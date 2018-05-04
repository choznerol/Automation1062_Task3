import cv2
import numpy as np
import time

"""
def CameraCapture():
    cp0 = cv2.VideoCapture(0)
    while 1:
        ret0, frame0 = cp0.read()
	cv2.imshow('Test0', frame0)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cp0.release()
"""

def DetermineColor_FindCircles(img):
    length, width, _ = img.shape
    color = None
    circles = []
    
    # TODO

    # TODO: Set & apply thresholds for each channel

    # TODO: Determine color

    # TODO: find circles

    return color, circles

def markcircles(img, circles):
    # No need to modify anything in this

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img, (i[0],i[1]),i[2],(0,0,0),2) 
        cv2.circle(img, (i[0],i[1]),2,(255,255,255),3)
    

image = cv2.imread('./src/red3.jpg')
circles_found, color_found = DetermineColor_FindCircles(image)

markcircles(image, circles_found)
print(color_found)

cv2.imshow('Task3', image)
cv2.imwrite('Task3_example.jpg', image)
