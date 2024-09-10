from adafruit_servokit import ServoKit
import time
import math
kit = ServoKit(channels=16)


# pan = 0


# while pan < 170:
#     pan += 10
#     kit.servo[0].angle = pan
#     time.sleep(1)


# def compute_joint1(X,Y):


#     theta1 = math.atan2(Y,X)

#     return theta1

# X_desired = 0
# Y_desired = 5

# X_compute = X_desired - 90
# Y_compute = Y_desired 

# theta1 = compute_joint1(X_compute,Y_compute)

# print(f"required rotation in radians: {theta1}")
# print(f"Required rotation in degrees: {math.degrees(theta1)}")



modi = (-1)
x = 175 
g = 5000
kit.servo[0].angle = 0
while g > 100:
    x += modi
    y = math.sqrt(((90**2)-((x-90)**2)))
    
    
    x_compute = x - 90
    calc = math.atan2(y,x_compute)
    compute = math.degrees(calc)

    
    kit.servo[0].angle = compute
    time.sleep(0.005)



    print(f"compute:{compute}")
    print(f"x:{x}")
    print(f"y:{y}")
    
    if x == 2 or x==175:
        modi = modi * (-1)
    g -=1

kit.servo[0].angle = 0