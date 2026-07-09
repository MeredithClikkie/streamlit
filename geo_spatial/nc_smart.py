import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("North Carolina Statewide Geo Visualization")

# NC bounding box
lat_min, lat_max = 33.8, 36.6
lon_min, lon_max = -84.3, -75.5

# Random statewide points
chart_data = pd.DataFrame({
    "lat": np.random.uniform(lat_min, lat_max, 1500),
    "lon": np.random.uniform(lon_min, lon_max, 1500)
})

st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=35.5,
            longitude=-79.0,
            zoom=6.5,
            pitch=45,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=15000,
                elevation_scale=20,
                elevation_range=[0, 3000],
                pickable=True,
                extruded=True,
            )
        ],
    )
)
