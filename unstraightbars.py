import cv2

dispW=320
dispH=240



def nothing(x):
    pass

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cv2.namedWindow('LogiCam')


cv2.createTrackbar('x','LogiCam',0, 320, nothing)
cv2.createTrackbar('y','LogiCam',0,240,nothing)
cv2.createTrackbar('xsize', 'LogiCam',0,100,nothing)
cv2.createTrackbar('ysize','LogiCam',0,100,nothing)

while True: 
    ret, frame=cam.read()
    
    xval = cv2.getTrackbarPos('x','LogiCam')
    yval = cv2.getTrackbarPos('y','LogiCam')
    xs = cv2.getTrackbarPos('xsize', 'LogiCam')
    ys = cv2.getTrackbarPos('ysize', 'LogiCam')
    
    
    
    cv2.rectangle(frame,(xval, yval),(xval+xs,yval+ys),(255,0,0),3)
   
    cv2.imshow('LogiCam', frame)   
    cv2.moveWindow('LogiCam', 0, 0)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()