import cv2

dispW=640
dispH=480




cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

xpos = 1
ypos = 1
BH = 70
BW = 70
dx = 3
dy = 3


while True: 
    ret, frame=cam.read()
    
    roi = frame[ypos:(ypos+BH),xpos:(xpos+BW)].copy()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[ypos:(ypos+BH),xpos:(xpos+BW)] = roi

    cv2.rectangle(frame,(xpos,ypos),(xpos + BW, ypos+ BH),(255,255,255),4)


    if xpos <= 0 or xpos + BW >= 640:
        dx = dx * -1

    if ypos <=0 or ypos + BH >= 480:
        dy = dy * -1

    frame = cv2.rectangle(frame,(xpos,ypos),(xpos + BW, ypos+ BH),(255,255,255),4)

    


    

    xpos += dx
    ypos += dy


    

    cv2.imshow('LogiCam', frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()