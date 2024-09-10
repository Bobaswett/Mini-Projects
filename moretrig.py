from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import math
import time




L1=70
L2=105
L3=100
L1_height = 55



def calc_J1(x):
    y = math.sqrt(((90**2)-((x-90)**2)))
    x_compute = x - 90
    calc = math.atan2(y,x_compute)
    dgs = math.degrees(calc)
    return dgs

def calc_J3(y,z):
    
    y_effective = y+100
    
    z_effective = z-L1_height

    
    D = math.sqrt((y_effective**2)+(z_effective**2))
    A3 = math.acos(((L2**2)+(L3**2)-(D**2))/(2*L2*L3))
    degrees = math.degrees(A3)
    return degrees 



def calc_J2(y,z):
    y_effective = y +100
    
    z_effective = z - L1_height

    
    D = math.sqrt((y_effective**2)+(z_effective**2))
    
    alpha = math.atan2(z_effective,y_effective)
    beta = math.acos(((L2**2)+(D**2)-(L3**2))/(2*L2*D))
    A2 = beta + alpha
    dgs = math.degrees(A2)
    return 90-dgs

print(calc_J1(150))
print(calc_J2(80,0))
print(calc_J3(80,0))

kit.servo[0].angle = calc_J1(150)
time.sleep(1)
kit.servo[1].angle = calc_J2(80,0)
time.sleep(1)
kit.servo[2].angle = calc_J2(80,0)
time.sleep(1)

time.sleep(5)

kit.servo[0].angle = 0
time.sleep(1)
kit.servo[1].angle = 0
time.sleep(1)
kit.servo[2].angle = 0
time.sleep(1)

