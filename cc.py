import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')



cv2.createTrackbar('hueLow','Trackbars',50,179,nothing)
cv2.createTrackbar('hueHigh','Trackbars',100,179,nothing)
cv2.createTrackbar('satLow','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)

dispW=320
dispH=240




# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    # ret, frame=cam.read()
    
    frame =cv2.imread('smarties.png')
     
    cv2.imshow('LogiCam', frame)
    cv2.moveWindow('LogiCam',0,0)
   
    hsv2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    hL = cv2.getTrackbarPos('hueLow','Trackbars')
    hU = cv2.getTrackbarPos('hueHigh','Trackbars')

    sL = cv2.getTrackbarPos('satLow','Trackbars')
    sU = cv2.getTrackbarPos('satHigh','Trackbars')

    vL = cv2.getTrackbarPos('valLow','Trackbars')
    vU = cv2.getTrackbarPos('valHigh','Trackbars')


    l_b = np.array([hL,sL,vL])
    u_b = np.array([hU,hU,vU])


    

    FGmask = cv2.inRange(hsv2,l_b,u_b)
    cv2.imshow('FGmask',FGmask)
    cv2.moveWindow('FGmask',0,410)


    FG = cv2.bitwise_and(frame, frame, mask = FGmask)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',480,0)


    BG = cv2.bitwise_not(FGmask)
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',480,410)

    BGMask = cv2.cvtColor(BG,cv2.COLOR_GRAY2BGR)

    final = cv2.add(FG,BGMask)
    cv2.imshow('final',final)
    cv2.moveWindow('final',900,0)
    cv2.moveWindow('Trackbars',900,410)
    if cv2.waitKey(1) ==ord('q'):
        break

# cam.release()
cv2.destroyAllWindows()
