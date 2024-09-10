import cv2

dispW=320
dispH=240




cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    ret, frame=cam.read()
    frame = cv2.rectangle(frame,(140,100),(180,140),(255,0,0),4)
    frame = cv2.circle(frame,(160, 120), 50, (0,0,255))

    cv2.imshow('LogiCam', frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
