
from picarx_improved import *
import time


def random_movement():
    print("angle 0")
    set_dir_servo_angle(0)
    forward(50)
    time.sleep(4)
    print("angle 20")
    set_dir_servo_angle(20)
    forward(50)
    time.sleep(4)
    print("angle  -40")
    set_dir_servo_angle(-40)
    forward(50)
    time.sleep(4)

def parallel_parking_left():
    set_dir_servo_angle(0)
    forward(50)
    time.sleep(1)
    set_dir_servo_angle(-20)
    backward(40)
    time.sleep(1)
    set_dir_servo_angle(20)
    backward(20)
    time.sleep(1)
    set_dir_servo_angle(0)
    forward(50)
    time.sleep(.5)
    stop()
    time.sleep(10)

def parallel_parking_right():
    set_dir_servo_angle(0)
    forward(50)
    time.sleep(1)
    set_dir_servo_angle(20)
    backward(40)
    time.sleep(1)
    set_dir_servo_angle(-20)
    backward(20)
    time.sleep(1)
    set_dir_servo_angle(0)
    forward(50)
    time.sleep(.5)
    stop()
    time.sleep(10)
    

def three_point_turn():
    set_dir_servo_angle(-40)
    forward(50)
    time.sleep(1)
    set_dir_servo_angle(40)
    backward(50)
    time.sleep(1)
    set_dir_servo_angle(0)
    forward(50)
    time.sleep(2)
    stop()
    backward(50)
    time.sleep(1)
    stop()
    time.sleep(10)

done = False
options = ["1","2","3","4","5"]
while(done == False):
    print("Please enter 1 random movement, 2 for parallel parking right, 3 for parallel parking left, 4 for Three-Point-Turn or 5 for exit")
    inputstring = input()
    if not (inputstring in options):
        print("invalid input")
    else:
        if inputstring == "1":
           random_movement()
        elif inputstring == "2":
           parallel_parking_left()
        elif inputstring == "3":
            parallel_parking_right()
        elif input == "4":
            three_point_turn()
        else:
            done = True

                    

