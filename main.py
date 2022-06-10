import numpy as np
import pandas as pd
import cv2

# defining the image
image = cv2.imread("image.jpg")

# defining the index of the .csv
index=["color", "color_name", "hex", "R", "G", "B"]

# defining the colors
colors = pd.read_csv('colors.csv', names=index, header=None)
