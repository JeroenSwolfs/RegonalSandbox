import geopandas as gpd
from shapely.geometry import box
import pandas as pd

# Define sandbox (in meters, RD New projection)
minx, miny, maxx, maxy = 0, 300000, 280000, 625000  # covers NL roughly
cell_size = 5000  # 5 km grid cells

cells = []
data = []

x = minx
while x < maxx:
    y = miny
    while y < maxy:
        geom = box(x, y, x + cell_size, y + cell_size)
        cells.append(geom)

        # Store useful metadata
        data.append({
            "xmin": x,
            "ymin": y,
            "xmax": x + cell_size,
            "ymax": y + cell_size,
            "xcenter": x + cell_size / 2,
            "ycenter": y + cell_size / 2
        })
        y += cell_size
    x += cell_size

# Build GeoDataFrame
grid = gpd.GeoDataFrame(data, geometry=cells, crs="EPSG:28992")

# Save for later use
grid.to_file("sandbox_grid.gpkg", driver="GPKG")

# Quick check
print(grid.head())

import folium

# Reproject to WGS84 (needed for web maps)
grid_wgs = grid.to_crs(epsg=4326)

# Center map roughly on NL
m = folium.Map(location=[52.1, 5.3], zoom_start=7)

m.save("sandbox_grid.html")
