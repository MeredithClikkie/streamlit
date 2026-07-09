You’ve got **four types of geospatial files** you can use in your NC apps — **GeoJSON**, **Shapefiles**, and **CSV with lat/lon** — and you can get them easily from **trusted public sources**, **Python libraries**, or **your own exports**.

Here’s the complete breakdown, organized by usefulness, with Guided Links on every actionable concept.

---

# 🟦 1. **GeoJSON files**
GeoJSON is the easiest format for Streamlit + PyDeck. You can get NC GeoJSON files from:

### Public sources
- **NC counties GeoJSON**
  `https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json` [(raw.githubusercontent.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fraw.githubusercontent.com%2Fplotly%2Fdatasets%2Fmaster%2Fgeojson-counties-fips.json")
- **US Census TIGER/Line GeoJSON**
  `https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html` [(census.gov in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.census.gov%2Fgeographies%2Fmapping-files%2Ftime-series%2Fgeo%2Ftiger-line-file.html")
- **OpenStreetMap via Overpass API**
  You can export any region as GeoJSON.

### Python generation
You can generate GeoJSON directly using GeoPandas:

```python
import geopandas as gpd

gdf = gpd.read_file("your_shapefile.shp")
gdf.to_file("output.geojson", driver="GeoJSON")
```

### GIS tools
- QGIS → “Export → Save Features As → GeoJSON”
- ArcGIS → “Export → GeoJSON”

---

# 🟩 2. **Shapefiles**
Shapefiles are the most common GIS format. They come as a **.zip** containing:

- `.shp` — geometry
- `.shx` — index
- `.dbf` — attributes
- `.prj` — projection

### Where to get NC shapefiles
- **NC OneMap (official)**
  [https://www.nconemap.gov](https://www.nconemap.gov)
  → Counties, roads, parcels, hydrography, schools, voting districts, etc.

- **US Census TIGER/Line**
  `https://www.census.gov/cgi-bin/geo/shapefiles/index.php` [(census.gov in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.census.gov%2Fcgi-bin%2Fgeo%2Fshapefiles%2Findex.php")
  → Counties, tracts, block groups, roads, rail, water, ZIP codes.

- **OpenStreetMap via Geofabrik**
  `https://download.geofabrik.de/north-america/us/north-carolina.html` [(download.geofabrik.de in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdownload.geofabrik.de%2Fnorth-america%2Fus%2Fnorth-carolina.html")
  → Roads, buildings, land use, natural features.

### Python conversion
Convert shapefile → GeoJSON:

```python
import geopandas as gpd

gdf = gpd.read_file("nc_counties.shp")
gdf.to_file("nc_counties.geojson", driver="GeoJSON")
```

---

# 🟧 3. **CSV with lat/lon**
CSV is the simplest format for point data.

### Ways to get NC CSV point data
- **Export from Google Maps MyMaps**
  → “Export as CSV”

- **OpenStreetMap Overpass Turbo**
  → Query POIs (schools, hospitals, parks)
  → Export → CSV

- **NC Open Data Portal**
  `https://data-nc.opendata.arcgis.com` [(data-nc.opendata.arcgis.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdata-nc.opendata.arcgis.com%2F")
  → Many datasets include lat/lon columns.

- **Your own data**
  If you have addresses, you can geocode them:

```python
from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="nc_mapper")

df = pd.read_csv("addresses.csv")

df["coords"] = df["address"].apply(lambda x: geolocator.geocode(x))
df["lat"] = df["coords"].apply(lambda x: x.latitude if x else None)
df["lon"] = df["coords"].apply(lambda x: x.longitude if x else None)

df.to_csv("nc_points.csv", index=False)
```

---

# 🟥 4. **Road network data**
For your NC road network visualization, the best source is **OSMnx**, which downloads OpenStreetMap data automatically.

### Python (recommended)
```python
import osmnx as ox

G = ox.graph_from_place("Charlotte, North Carolina", network_type="drive")
nodes, edges = ox.graph_to_gdfs(G)
edges.to_file("charlotte_roads.geojson", driver="GeoJSON")
```

### Other sources
- **NC DOT GIS Data**
  `https://connect.ncdot.gov/resources/gis/Pages/GIS-Data.aspx` [(connect.ncdot.gov in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fconnect.ncdot.gov%2Fresources%2Fgis%2FPages%2FGIS-Data.aspx")
- **Geofabrik NC extract**
  `https://download.geofabrik.de/north-america/us/north-carolina.html` [(download.geofabrik.de in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdownload.geofabrik.de%2Fnorth-america%2Fus%2Fnorth-carolina.html")

---

# 🟪 5. **Real NC datasets you can download right now**
Here are direct, high‑quality datasets you can use immediately:

### Counties
- NC county boundaries (GeoJSON)
  `https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json` [(raw.githubusercontent.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fraw.githubusercontent.com%2Fplotly%2Fdatasets%2Fmaster%2Fgeojson-counties-fips.json")

### Roads
- NC roads (Shapefile)
  `https://download.geofabrik.de/north-america/us/north-carolina.html` [(download.geofabrik.de in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdownload.geofabrik.de%2Fnorth-america%2Fus%2Fnorth-carolina.html")

### Population
- Census block group population (Shapefile + CSV)
  `https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html` [(census.gov in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.census.gov%2Fgeographies%2Fmapping-files%2Ftime-series%2Fgeo%2Ftiger-line-file.html")

### Schools
- NC public schools (CSV + lat/lon)
  `https://www.nconemap.gov/datasets/nc-public-schools` [(nconemap.gov in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.nconemap.gov%2Fdatasets%2Fnc-public-schools")

### Hospitals
- NC hospitals (CSV + lat/lon)
  `https://data-nc.opendata.arcgis.com` [(data-nc.opendata.arcgis.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdata-nc.opendata.arcgis.com%2F")

---

# 🟦 Want me to build a **data downloader** inside your Streamlit app?

Choose one:

- NC dataset downloader UI
- NC geospatial file converter
- NC shapefile → GeoJSON auto‑converter

Tell me which one you want next.
