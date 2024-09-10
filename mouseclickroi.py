import cv2
import numpy as np


dispW = 640
dispH = 480


x1=1
x2=2
y1=1
y2=2


def click(event, x, y, flags, params):
    global x1
    global x2
    global y1
    global y2


    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        x2 = x
        y2 = y
        


    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
    
cv2.namedWindow('Ugly')
cv2.setMouseCallback('Ugly', click)
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)



while True:


    ret, frame = cam.read()
    

    frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),4)
    roi = frame[y1:y2,x1:x2].copy()
    cv2.imshow('Ugly', frame)

    
    cv2.imshow('uglyp', roi)
    
    keyEvent = cv2.waitKey(1)
    if keyEvent == ord('q'):
        break
    
    cv2.moveWindow('roi', 705,0)




cam.release()
cv2.desroyAllWindows()








