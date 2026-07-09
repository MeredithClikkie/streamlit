import streamlit as st
import geopandas as gpd
import pydeck as pdk
import pandas as pd
import numpy as np

st.title("North Carolina County‑Level Choropleth")

# Load NC county shapefile
url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
counties = gpd.read_file(url)

# Filter NC (state FIPS = 37)
nc = counties[counties["STATE"] == "37"]

# Fake metric for demo
nc["value"] = np.random.randint(10, 100, len(nc))

# Convert to PyDeck format
nc_json = nc.to_json()

layer = pdk.Layer(
    "GeoJsonLayer",
    nc_json,
    opacity=0.6,
    stroked=True,
    filled=True,
    get_fill_color="[value * 2, 100, 150, 180]",
    get_line_color="[255, 255, 255]",
)

view_state = pdk.ViewState(
    latitude=35.5,
    longitude=-79.0,
    zoom=6,
    pitch=0,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
