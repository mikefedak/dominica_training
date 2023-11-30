#output USGS data to geojson files 

import requests, geopandas as gp, json
from datetime import datetime, timedelta

base_url='https://earthquake.usgs.gov/fdsnws/event/1/query'
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 11, 26)  # Change this to the end date you want

params={'format':'geojson','minlatitude':'9.014','maxlatitude':'20.393','minlongitude':'-73.882','maxlongitude':'-57.524'}


# Loop over the dates
current_date = start_date
while current_date <= end_date:
    params['starttime'] = current_date.strftime('%Y-%m-%d')
    params['endtime'] = (current_date + timedelta(days=1)).strftime('%Y-%m-%d')

    earthquakes=requests.get(base_url,params=params)

    out_name = f'usgs_earthquakes_{current_date.strftime("%Y-%m-%d") }.geojson'
    with open('./earthquake_example/'+out_name, 'w') as f:
        json.dump(earthquakes.json(), f)

    # Move to the next date
    current_date += timedelta(days=1)