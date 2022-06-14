import numpy as np
import pandas as pd
import cv2
import pyperclip

# defining the image
# your_image = input("Please enter your image name: ")
image = cv2.imread(input("Please enter your image: "))

# defining the index of the .csv
index=["color", "color_name", "hex", "R", "G", "B"]

# defining the colors
colors = pd.read_csv('colors.csv', names=index, header=None)

# defining global variables
clicked = False
r = g =b = xpos = ypos = 0

# this function uses the colors.csv file that was loaded to return the color name and RGB value
def recognize_color(R, G, B):
    minimum = 10000
    for i in range(len(colors)):
        d = abs(R- int(colors.loc[i, "R"])) + abs(G- int(colors.loc[i, "G"])) + abs(B- int(colors.loc[i, "B"]))
        if(d<=minimum):
            minimum = d
            colorname = colors.loc[i, "color_name"]
    return colorname

# this function triggers the mouse_click event 
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r, = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# this section copies the rgb(r, g, b) value to the clipboard automatically
def copy_rgb(r, g, b):
    pyperclip.copy('rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')')

# this section creates the window with the image inside
cv2.namedWindow('Kaleidoscope Eyes')
cv2.setMouseCallback('Kaleidoscope Eyes', mouse_click)

# while loop that starts the application and keeps it running
while(1):
    cv2.imshow("Kaleidoscope Eyes", image)
    if (clicked):
        cv2.rectangle(image,(20,20), (750,60), (b,g,r), -1)
        text = recognize_color(r,g,b) + ' R='+ str(r) + ' G='+str(g) + ' B='+ str(b)
        cv2.putText(image, text, (50,50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        copy_rgb(r, g, b)

    if (r+g+b>=600):
        cv2.putText(image, text, (50, 50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
        clicked=False

    if cv2.waitKey(20) & 0xFF ==27:
        break

# closes window
cv2.destroyAllWindows()