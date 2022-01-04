import cv2.cv2 as cv2
import numpy as np

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        colordetect = np.zeros((512, 512, 3), np.uint8)
        colordetect [:] = [blue, green, red]
        
        cv2.imshow('color', colordetect)

img = cv2.imread('Images\RYB.png')
cv2.imshow('ImageWindow', img)
points = []
cv2.setMouseCallback('ImageWindow', mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()
