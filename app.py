import streamlit as st
import plotly.express as px
from PIL import Image

from data_loader import load_all_data
from coordinate_mapper import world_to_minimap
from config import MAP_CONFIG

st.set_page_config(layout="wide")

st.title("LILA Player Journey Visualization Tool")

DATA_PATH = "data/player_data"

@st.cache_data
def load_data():
    return load_all_data(DATA_PATH)

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

maps = df["map_id"].unique()
selected_map = st.sidebar.selectbox("Map", maps)

map_df = df[df["map_id"] == selected_map]

matches = map_df["match_id"].unique()
selected_match = st.sidebar.selectbox("Match", matches)

match_df = map_df[map_df["match_id"] == selected_match]

player_types = st.sidebar.multiselect(
    "Player Type",
    ["Human", "Bot"],
    default=["Human", "Bot"]
)

match_df = match_df[match_df["player_type"].isin(player_types)]

# Timeline
min_time = match_df["ts"].min()
max_time = match_df["ts"].max()

time_slider = st.sidebar.slider(
    "Timeline",
    min_value=min_time,
    max_value=max_time,
    value=max_time
)

match_df = match_df[match_df["ts"] <= time_slider]

# Coordinate Mapping
config = MAP_CONFIG[selected_map]

pxs = []
pys = []

for _, row in match_df.iterrows():

    x = row["x"]
    z = row["z"]

    px, py = world_to_minimap(
        x,
        z,
        config["scale"],
        config["origin_x"],
        config["origin_z"]
    )

    pxs.append(px)
    pys.append(py)

match_df["px"] = pxs
match_df["py"] = pys

# Map Display
image = Image.open(config["image"])

fig = px.scatter(
    match_df,
    x="px",
    y="py",
    color="player_type",
    hover_data=["event"],
)

fig.update_layout(
    images=[
        dict(
            source=image,
            xref="x",
            yref="y",
            x=0,
            y=1024,
            sizex=1024,
            sizey=1024,
            sizing="stretch",
            opacity=0.7,
            layer="below"
        )
    ]
)

fig.update_yaxes(autorange="reversed")

st.plotly_chart(fig, use_container_width=True)

# Event Markers
st.subheader("Event Markers")

events = match_df[
    match_df["event"].isin(
        ["Kill", "Killed", "Loot", "KilledByStorm"]
    )
]

event_fig = px.scatter(
    events,
    x="px",
    y="py",
    color="event"
)

event_fig.update_yaxes(autorange="reversed")

st.plotly_chart(event_fig, use_container_width=True)

# Heatmap
st.subheader("Traffic Heatmap")

heatmap = px.density_heatmap(
    match_df,
    x="px",
    y="py",
    nbinsx=50,
    nbinsy=50
)

st.plotly_chart(heatmap, use_container_width=True)