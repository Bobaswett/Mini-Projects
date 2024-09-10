import cv2

dispW=640
dispH=480




cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True: 
    ret, frame=cam.read()

    roi = frame[50:250,200:400].copy()

    roigrey = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    frame[50:400,200:400] = [255, 255, 255]
    cv2.imshow('roi', roi)
    
    cv2.imshow('LogiCam', frame)
    cv2.imshow('roigrey', roigrey)

    if cv2.waitKey(1) ==ord('q'):
        break
    cv2.moveWindow('roi', 0, 1000)
    cv2.moveWindow('LogiCam', 0,0)
    cv2.moveWindow('roigrey', 1000, 0)
cam.release()
cv2.destroyAllWindows()
