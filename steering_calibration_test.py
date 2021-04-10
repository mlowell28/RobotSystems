
from picarx_improved import *
from ezblock import *
#from ezblock import __reset_mcu__
import time
#__reset_mcu__()
time.sleep(1)

while(1):
     set_dir_servo_angle(0)
     forward(70)
     time.sleep(2)
     stop()
     time.sleep(2)
     set_dir_servo_angle(-30)
     backward(70)
     time.sleep(2)
     set_dir_servo_angle(30)
     backward(70)
     time.sleep(2)
     set_dir_servo_angle(30)
     forward(70)
     time.sleep(2)
     set_dir_servo_angle(-30)
     forward(70)
     time.sleep(2)


