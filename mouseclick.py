import cv2
import numpy as np
evt = -1
coord = []
rgb = []
def click(event,x,y,flags,params):
    global pnt 
    global evt
    global rgb
    global color
    global pnt2
    global blue
    global red
    global green
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(event)
        # print(x,y)
        
        pnt = (x,y)
        evt = event
        coord.append(pnt)
    if event == cv2.EVENT_RBUTTONDOWN:
        # print(x, y)
        pnt2 = (x,y)
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        color = (blue+','+green+","+red)
        evt = event
        rgb.append(color)

dispW=320
dispH=240


cv2.namedWindow('LogiCam')
cv2.setMouseCallback('LogiCam', click)





cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    ret, frame=cam.read()
    
    for pnts in coord: #wont step into loop unless there are coordinates in array coord
        cv2.circle(frame, pnts, 5, (0,0,255), -1)
        font = cv2.FONT_HERSHEY_PLAIN
        myStr = str(pnts)
        
        cv2.putText(frame,myStr, pnts, font, 1, (0,0,255), 2)
        print(coord)
    for colors in rgb:
        myStr2 = str(blue+''+green+""+ red)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,myStr2, pnt2, font, 1, (0,0,255), 2)
        print(rgb)
    cv2.imshow('LogiCam', frame)
    keyEvent = cv2.waitKey(1)
    if keyEvent ==ord('q'):
        break
    if keyEvent == ord('c'):
        coord = []   
cam.release()
cv2.destroyAllWindows()
0