import time
from math import *
import logging
from logdecorator import log_on_start, log_on_end, log_on_error
import atexit 

try:
     from ezblock import *
     from ezblock import __reset_mcu__
     __reset_mcu__()
     time.sleep(0.01)
except ImportError:
     print("This computer does not appear to be a PiCar-X system(/opt/ezblock not present). Swithing to simulated hardware calls")
     from sim_ezblock import *

class MotorController()
     def __init__(self):
     self.period = 
          
