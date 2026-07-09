import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("North Carolina City Map Explorer")

cities = {
    "Charlotte": (35.2271, -80.8431),
    "Raleigh": (35.7796, -78.6382),
    "Durham": (35.9940, -78.8986),
    "Greensboro": (36.0726, -79.7920),
    "Wilmington": (34.2257, -77.9447),
    "Asheville": (35.5951, -82.5515),
}

city = st.selectbox("Choose a city", list(cities.keys()))
lat, lon = cities[city]

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [lat, lon],
    columns=["lat", "lon"]
)

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=lat,
            longitude=lon,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[0, 150, 255, 160]",
                get_radius=200,
            )
        ],
    )
)
