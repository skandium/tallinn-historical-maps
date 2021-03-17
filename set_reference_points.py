import cv2
import os
from tkinter import simpledialog, Tk
import csv
import argparse

master = Tk()

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
args = parser.parse_args()
map_file = args.file
map_path = os.path.join("map_files", map_file)
print(map_path)

reference_points_path = os.path.join("reference_points", map_file.split(".")[0] + "_reference_points.csv")
header = ["x", "y", "lon", "lat", "name"]
# Save header for reference points if file does not exist
if not os.path.exists(reference_points_path):
    with open(reference_points_path, 'w') as outheader:
        writer = csv.writer(outheader)
        writer.writerow(header)


# click event function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        coords = simpledialog.askstring("Add reference point", "Enter lat, lon, name:")
        lat, lon, name = coords.split(", ")
        row = [x, y, float(lon), float(lat), name]
        print(row)

        with open(reference_points_path, "a") as outrow:
            writer = csv.writer(outrow)
            writer.writerow(row)
    else:
        pass


# Here, you need to change the image name and it's path according to your directory
img = cv2.imread(map_path)
cv2.imshow("image", img)

# calling the mouse click event
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
