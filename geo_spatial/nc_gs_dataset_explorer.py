import streamlit as st
import geopandas as gpd
import pandas as pd
import pydeck as pdk

st.title("North Carolina Geospatial Dataset Explorer")

uploaded = st.file_uploader("Upload GeoJSON, Shapefile (.zip), or CSV", type=["geojson", "zip", "csv"])

if uploaded:
    if uploaded.name.endswith(".geojson"):
        gdf = gpd.read_file(uploaded)
    elif uploaded.name.endswith(".zip"):
        gdf = gpd.read_file(uploaded)
    else:
        df = pd.read_csv(uploaded)
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))

    st.write(gdf.head())

    layer = pdk.Layer(
        "GeoJsonLayer",
        gdf.to_json(),
        opacity=0.7,
        stroked=True,
        filled=True,
        get_fill_color="[100, 150, 240, 180]",
        get_line_color="[255, 255, 255]",
    )

    view_state = pdk.ViewState(
        latitude=35.5,
        longitude=-79.0,
        zoom=6,
        pitch=0,
    )

    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
