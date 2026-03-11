# LILA Player Journey Visualization Tool

Live Demo:
https://lila-games-project.streamlit.app/

This tool visualizes player movement, combat events, and heatmaps from gameplay telemetry to help Level Designers understand player behavior across maps.

---

## Features

- Player movement visualization
- Human vs Bot detection
- Kill, death, loot, storm markers
- Timeline playback of matches
- Heatmaps for traffic and combat zones
- Filtering by map, date, and match

---

## Tech Stack

Python  
Streamlit  
Pandas  
PyArrow  
Plotly  

---

## Run Locally

Clone the repository

git clone https://github.com/niharikabhatia/LILA-GAMES-PROJECT.git

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

---

## Project Structure

app.py — main visualization app  
data_loader.py — telemetry loader  
coordinate_mapper.py — map coordinate conversion  
config.py — map configurations  

---

## Deployment

The tool is deployed on Streamlit Cloud.

Live URL:
https://lila-games-project.streamlit.app/