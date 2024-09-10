import cv2

dispW=320
dispH=240




cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)


xpos = 1
ypos = 1
BH = 30
BW = 70
dx = 3
dy = 3


while True: 
    ret, frame=cam.read()
    
    if xpos <= 0 or xpos+ BW >= 320:
        dx = dx * -1
    
    if ypos <= 0 or ypos + BH >= 240:
        dy = dy * -1
    
    frame = cv2.rectangle(frame,(xpos,ypos),(xpos + BW,ypos + BH),(255,0,0),4)

    xpos += dx
    ypos += dy
    # frame = cv2.circle(frame,(160, 120), 50, (0,0,255))

    cv2.imshow('LogiCam', frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
