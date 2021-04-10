\
from custom_picarx_controller import *
import time


def random_movement(controller):
    controller.set_dir_servo_angle(0)
    controller.forward(50)
    time.sleep(4)
    controller.set_dir_servo_angle(20)
    controller.forward(50)
    time.sleep(4)
    controller.set_dir_servo_angle(-20)
    controller.forward(50)
    time.sleep(4)

def parallel_parking_left(controller):
    controller.set_dir_servo_angle(0)
    controller.forward(50)
    time.sleep(1)
    controller.set_dir_servo_angle(-20)
    controller.backward(40)
    time.sleep(1)
    controller.set_dir_servo_angle(20)
    controller.backward(20)
    time.sleep(1)
    controller.set_dir_servo_angle(0)
    controller.forward(50)
    time.sleep(.5)
    controller.stop()
    time.sleep(10)

def parallel_parking_right(controller):
    controller.set_dir_servo_angle(0)
    controller.forward(50)
    time.sleep(1)
    controller.set_dir_servo_angle(20)
    controller.backward(40)
    time.sleep(1)
    controller.set_dir_servo_angle(-20)
    controller.backward(20)
    time.sleep(1)
    controller.set_dir_servo_angle(0)
    controller.forward(50)
    time.sleep(.5)
    controller.stop()
    time.sleep(10)
    

def three_point_turn(controller):
    controller.set_dir_servo_angle(-40)
    controller.forward(50)
    time.sleep(1)
    controller.set_dir_servo_angle(40)
    controller.backward(50)
    time.sleep(1)
    controller.set_dir_servo_angle(0)
    controller.forward(50)
    controller.time.sleep(2)
    stop()
    controller.backward(50)
    time.sleep(1)
    controller.stop()
    time.sleep(10)

done = False
options = ["1","2","3","4","5"]

my_controller = MotorController()

while(done == False):
    print("Please enter 1 random movement, 2 for parallel parking right, 3 for parallel parking left, 4 for Three-Point-Turn or 5 for exit")
    inputstring = input()
    if not (inputstring in options):
        print("invalid input")
    else:
        if inputstring == "1":
           random_movement(my_controller)
        elif inputstring == "2":
           parallel_parking_left(my_controller)
        elif inputstring == "3":
            parallel_parking_right(my_controller)
        elif input == "4":
            three_point_turn(my_controller)
        else:
            done = True

                    

