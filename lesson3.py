import cv2

dispWidth=320
dispHeight=240




cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispWidth)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispHeight)

while True: 
    ret, frame=cam.read()
    cv2.imshow('LogiCam', frame)
    cv2.moveWindow('LogiCam', 700, 0)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY    )
    
    frameSmall = cv2.resize(frame,(320,240))
    graySmall = cv2.resize(gray,(320,240))
    cv2.moveWindow('BW',0,265)
    cv2.moveWindow('Logismall',0,0)
    cv2.imshow('BW',graySmall)
    cv2.imshow('nanoSmall',frameSmall)
    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()