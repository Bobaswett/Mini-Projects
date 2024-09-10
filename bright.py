import os
import cv2

dispW = 320
dispH = 240

def nothing(x):
    pass

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cv2.namedWindow('LogiCam')

cv2.createTrackbar('brightness','LogiCam',1, 10, nothing)



while True: 
    # dval = cv2.getTrackbarPos('brightness','LogiCam')
    ret, frame=cam.read()
    f = cv2.getTrackbarPos('brightness','LogiCam')
    e = f /10
    g = f'xrandr --output HDMI-0 --brightness {e}'
    print(e)

    if cv2.waitKey(1) ==ord('t'):
        cmd = 'ls -l'
        os.system(g)
    cv2.imshow('LogiCam', frame)   
    cv2.moveWindow('LogiCam', 0, 0)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()