import cv2

dispW=320
dispH=240




cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    ret, frame=cam.read()
    cv2.imshow('LogiCam', frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
