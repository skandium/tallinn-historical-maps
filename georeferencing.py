import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import argparse
from sklearn.metrics import r2_score

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
args = parser.parse_args()
map_file = args.file

img = mpimg.imread(os.path.join("map_files", map_file))
reference_points_path = os.path.join("reference_points", map_file.split(".")[0] + "_reference_points.csv")

pts = pd.read_csv(reference_points_path)

lr_lat = LinearRegression()
lr_lat.fit(pts['y'].to_numpy().reshape(-1, 1), pts['lat'])

lr_lng = LinearRegression()
lr_lng.fit(pts['x'].to_numpy().reshape(-1, 1), pts['lon'])

bbox_lat = lr_lat.predict(np.array([0, img.shape[0]]).reshape(-1, 1)).round(4)
bbox_lon = lr_lng.predict(np.array([0, img.shape[1]]).reshape(-1, 1)).round(4)

print(f"Bounding box for {map_file}")
print(f"Bottom left: ({bbox_lat[1]}, {bbox_lon[0]})")
print(f"Top right: ({bbox_lat[0]}, {bbox_lon[1]})")

pred_lat = lr_lat.predict(np.array(pts['y']).reshape(-1, 1))
plt.plot(pts['y'], pred_lat)
plt.scatter(pts['y'], pts['lat'], color='red')
plt.annotate(f"R2: {round(r2_score(pts['lat'], pred_lat), 4)}", (min(pts['y']), max(pts['lat'])))
for i, txt in enumerate(pts):
    row = pts.iloc[i]
    plt.annotate(row["name"], (row["y"], pred_lat[i]))
plt.show()
