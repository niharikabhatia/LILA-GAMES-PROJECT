# Architecture Overview

## Tech Stack

Python
Streamlit
PyArrow
Pandas
Plotly

Streamlit was chosen for rapid development and easy deployment.

## Data Flow

Raw Parquet Files
↓
PyArrow Loader
↓
Event Decoding
↓
Bot Detection
↓
Coordinate Mapping
↓
Dataframe Aggregation
↓
Streamlit Visualization

## Coordinate Mapping

Game world coordinates are converted to minimap coordinates using:

u = (x - origin_x) / scale
v = (z - origin_z) / scale

pixel_x = u * 1024
pixel_y = (1 - v) * 1024

This maps world positions to minimap pixel positions.

## Tradeoffs

| Decision | Alternative | Reason |
|--------|--------|--------|
Streamlit | React | faster development |
Pandas | Spark | dataset small |
Local processing | DB | unnecessary complexity |

## Future Improvements

Player clustering
Path similarity detection
Bot AI analysis
Extraction success analytics