import streamlit as st
import osmnx as ox
import geopandas as gpd
import pydeck as pdk

st.title("North Carolina Road Network Visualization")

city = st.selectbox("Choose a city", ["Charlotte", "Raleigh", "Durham", "Greensboro", "Asheville", "Wilmington"])

# Download road network
G = ox.graph_from_place(f"{city}, North Carolina", network_type="drive")
gdf = ox.graph_to_gdfs(G, nodes=False, edges=True)

layer = pdk.Layer(
    "PathLayer",
    data=gdf,
    get_path="geometry.coordinates",
    get_color="[0, 150, 255]",
    width_scale=2,
    width_min_pixels=2,
)

view_state = pdk.ViewState(
    latitude=gdf.geometry.iloc[0].centroid.y,
    longitude=gdf.geometry.iloc[0].centroid.x,
    zoom=11,
    pitch=45,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
