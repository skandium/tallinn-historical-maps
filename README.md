# Georeferencing for image overlays in Python

0. Install depencencies `pip install -r requirements.txt`
1. Place raster image in `map_files` folder
2. Specify georeferencing points with `python set_reference_points.py --file MAP_FILE_NAME`. The UI currently assumes a 
   mouse click on the image and then comma-separated lat,lon,name for the desired reference point.
3. Get georeferenced bounding box from `python georeferencing.py --file MAP_FILE_NAME`. Also visualizes the fit quality
   and outlying points which you can then remove from the .csv file in `reference_points/`
4. Generate a html based on the template `html/leaflet_map.html`

Example outcome [here](https://skandium.github.io/tallinn-historical-maps/)