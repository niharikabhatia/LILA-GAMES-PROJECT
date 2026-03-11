 import plotly.express as px

def generate_heatmap(df):

    fig = px.density_heatmap(
        df,
        x="px",
        y="py",
        nbinsx=50,
        nbinsy=50
    )

    return fig