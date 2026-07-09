import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("North Carolina Population Heatmap")

# NC bounding box
lat_min, lat_max = 33.8, 36.6
lon_min, lon_max = -84.3, -75.5

# Generate weighted random points
n = 3000
chart_data = pd.DataFrame({
    "lat": np.random.uniform(lat_min, lat_max, n),
    "lon": np.random.uniform(lon_min, lon_max, n),
    "weight": np.random.exponential(scale=1.0, size=n)
})

layer = pdk.Layer(
    "HeatmapLayer",
    data=chart_data,
    get_position="[lon, lat]",
    get_weight="weight",
    radiusPixels=40,
)

view_state = pdk.ViewState(
    latitude=35.5,
    longitude=-79.0,
    zoom=6.5,
    pitch=45,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
