#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the required libraries
import requests
import json
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.tile_providers import get_provider, STAMEN_TERRAIN
import numpy as np
from bokeh.tile_providers import CARTODBPOSITRON
from bokeh.layouts import column
from bokeh.plotting import curdoc

# Function to convert GCS WGS84 to web mercator
def wgs84_to_web_mercator(lon, lat):
    k = 6378137
    x = lon * (k * np.pi / 180.0)
    y = np.log(np.tan((90 + lat) * np.pi / 360.0)) * k
    return x, y

# Function to convert individual lon and lat to web mercator
def wgs84_web_mercator_point(lon, lat):
    k = 6378137
    x = lon * (k * np.pi / 180.0)
    y = np.log(np.tan((90 + lat) * np.pi / 360.0)) * k
    return x, y

# Area extent coordinates in WGS84
lon_min, lat_min = -125.974, 30.038
lon_max, lat_max = -68.748, 52.214

# Coordinate conversion for extent coordinates
xy_min = wgs84_web_mercator_point(lon_min, lat_min)
xy_max = wgs84_web_mercator_point(lon_max, lat_max)

# Coordinate range in web mercator
x_range, y_range = ([xy_min[0], xy_max[0]], [xy_min[1], xy_max[1]])

# REST API query URL
user_name = ''
password = ''
url_data = f'https://{user_name}:{password}@opensky-network.org/api/states/all?lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}'

# Create a figure
p = figure(x_range=x_range, y_range=y_range, x_axis_type='mercator', y_axis_type='mercator', sizing_mode='scale_width', height=300)

# Add a tile provider (STAMEN_TERRAIN)
tile_prov = get_provider(CARTODBPOSITRON)
p.add_tile(tile_prov, level='image')

# Add hover tool
hover = HoverTool()
hover.tooltips = [("Call sign", "@callsign"), ("Origin Country", "@origin_country"), ("Velocity (m/s)", "@velocity"), ("Altitude (m)", "@baro_altitude")]
p.add_tools(hover)

# Define a ColumnDataSource
flight_source = ColumnDataSource(data={'icao24': [], 'callsign': [], 'origin_country': [],
                                       'time_position': [], 'last_contact': [], 'long': [], 'lat': [],
                                       'baro_altitude': [], 'on_ground': [], 'velocity': [], 'true_track': [],
                                       'vertical_rate': [], 'sensors': [], 'geo_altitude': [], 'squawk': [], 'spi': [],
                                       'position_source': [], 'x': [], 'y': [], 'rot_angle': [], 'url': []})

# Plot aircraft positions
p.image_url(url='url', x='x', y='y', source=flight_source, anchor='center', angle_units='deg', angle='rot_angle', w_units='screen', h_units='screen', w=40, h=40)
p.circle('x', 'y', source=flight_source, fill_color='red', hover_color='yellow', size=10, fill_alpha=0.8, line_width=0)

# Create a permanent top-level layout (a column in this case)
page = column()

# Add the top-level layout to curdoc
curdoc().add_root(page)

# Create a function for updating flight data
def update():
    response = requests.get(url_data).json()
    col_name = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'long', 'lat', 'baro_altitude', 'on_ground', 'velocity',
                'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source']

    flight_df = pd.DataFrame(response['states'])
    flight_df = flight_df.loc[:, 0:16]
    flight_df.columns = col_name

    # Add web mercator coordinates and other required columns to the DataFrame
    flight_df[['x', 'y']] = flight_df.apply(lambda row: pd.Series(wgs84_web_mercator_point(row['long'], row['lat'])), axis=1)
    flight_df['rot_angle'] = flight_df['true_track'] * -1

    # Replace 'NaN' with 'No Data'
    flight_df.fillna('No Data', inplace=True)

    # Define the URL for the airplane icon
    icon_url = 'https://news.aa.com/multimedia/logos/default.aspx'  # Replace with the actual URL of the airplane icon
    flight_df['url'] = icon_url

    # Stream the updated data to the ColumnDataSource
    flight_source.data = flight_df.to_dict(orient='list')

# Periodic callback to update flight data (every 5 seconds)
curdoc().add_periodic_callback(update, 5000)

# Show the plot
show(p)


# In[ ]:




