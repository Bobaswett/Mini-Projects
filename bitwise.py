import cv2
import numpy as np


dispW=640
dispH=480

#Initial Imgs 
img1 = np.zeros((480,640,1), np.uint8)
img1[0:480,0:320]=[255]

img2 = np.zeros((480,640,1), np.uint8)
img2[190:290,270:370] = [255]
bitAnd = cv2.bitwise_and(img1,img2)#outputs white if both are white
bitOr = cv2.bitwise_or(img1,img2)# outputs whites if AT LEAST one is white
bitXor = cv2.bitwise_xor(img1,img2)# outputs white if ONLY one is white

#CamSetup 
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    ret, frame=cam.read()
    frame=cv2.bitwise_and(frame,frame,mask=img1)

    cv2.imshow('LogiCam', frame)
    cv2.moveWindow('LogiCam',0,0)
    
    cv2.imshow('img1',img1)
    cv2.moveWindow('img1',0,500)
    
    cv2.imshow('img2',img2)
    cv2.moveWindow('img2',705,0)

    cv2.imshow('And',bitAnd)
    cv2.moveWindow('And',705, 500)
    
    cv2.imshow('or',bitOr)
    cv2.moveWindow('or', 300, 300)

    cv2.imshow('Xor', bitXor)

    


    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
