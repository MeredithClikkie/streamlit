import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.write("North Carolina Geo Visualization 🌄 Using PyDeck + Streamlit")

# Generate random points around Charlotte, NC
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [35.2271, -80.8431],
   columns=['lat', 'lon']
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=35.2271,
            longitude=-80.8431,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

import pkgutil
print("Streamlit version:", st.__version__)
print("Has proto module:", pkgutil.find_loader("streamlit.proto"))
