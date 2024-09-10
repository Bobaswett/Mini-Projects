import cv2

dispW=640
dispH=480




#cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('videos/myCam.avi')
#outVid = cv2.VideoWriter('videos/myCam.avi', cv2.VideoWriter_fourcc(*'XVID'),30,(dispW,dispH))
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    ret, frame=cam.read()
    cv2.imshow('LogiCam', frame)

    #outVid.write(frame)
    if cv2.waitKey(30) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()