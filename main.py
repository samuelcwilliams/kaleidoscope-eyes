import numpy as np
import pandas as pd
import cv2

# defining the image
image = cv2.imread("image.jpg")

# defining the index of the .csv
index=["color", "color_name", "hex", "R", "G", "B"]

# defining the colors
colors = pd.read_csv('colors.csv', names=index, header=None)

# defining global variables
clicked = False
r = g =b = xpos = ypos = 0

# this function uses the colors.csv file that was loaded to return the color name and RGB value
def recognize_color(R, G, B)
	minimum = 10000
	for i in range(len(colors)):
		d = abs(R- int(colors.loc[i, "R"])) + abs(G- int(colors.loc[i, "G"])) + abs(B- int(colors.loc[i, "B"])) 
		if(d<=minimum):
			minimum = d
			colorname = colors.loc[i, "color_name"]
	return colorname	

# this function triggers the mouse_click event 
def mouse_click(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y 
		b, g, r, = img[y, x]
		b = int(b)
		g = int(g)
		r = int(r)

# this section creates the window with the image inside
cv2.namedWindow('Kaleidoscope Eyes')
cv2.setMouseCallback('Kaleidoscope Eyes', mouse_click)
