import time
from math import *
import logging
from logdecorator import log_on_start, log_on_end, log_on_error
import atexit 

logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format , level=logging.INFO ,datefmt ="%H:%M:%S")
logging.getLogger ().setLevel(logging.DEBUG)

try:
     from ezblock import *
     from ezblock import __reset_mcu__
     __reset_mcu__()
     time.sleep(0.01)
except ImportError:
     print("This computer does not appear to be a PiCar-X system(/opt/ezblock not present). Swithing to simulated hardware calls")
     from sim_ezblock import *

class MotorController:
     def __init__(self):
 
          self.PERIOD = 4095
          self.PRESCALER = 10
          self.TIMEOUT = 0.02
          self.steering_angle = 0

          self.dir_servo_pin = Servo(PWM('P2'))
          self.camera_servo_pin1 = Servo(PWM('P0'))
          self.camera_servo_pin2 = Servo(PWM('P1'))
          self.left_rear_pwm_pin = PWM("P13")
          self.right_rear_pwm_pin = PWM("P12")
          self.left_rear_dir_pin = Pin("D4")
          self.right_rear_dir_pin = Pin("D5")

          self.Servo_dir_flag = 1
          self.dir_cal_value = -5.5
          self.cam_cal_value_1 = 0
          self.cam_cal_value_2 = 0
          self.motor_direction_pins = [self.left_rear_dir_pin, self.right_rear_dir_pin]
          self.motor_speed_pins = [self.left_rear_pwm_pin, self.right_rear_pwm_pin]
          self.cali_dir_value = [1, -1]
          self.cali_speed_value = [0, 0]

          for pin in self.motor_speed_pins:
               pin.period(self.PERIOD)
               pin.prescaler(self.PRESCALER)
          
          atexit.register(self.cleanup)

     @log_on_start(logging.DEBUG , "set_motor_speed started, motor: {motor:f}, speed: {speed:f}")
     @log_on_error(logging.DEBUG , "set_motor_speed  encountersan error  before  completing ")
     @log_on_end(logging.DEBUG , "set_motor_speed completed")
     def set_motor_speed(self, motor, speed):
          logging.debug('setting motor speed, motor: %f, speed: %f', motor, speed)
          motor -= 1
          if speed >= 0:
               direction = 1 * self.cali_dir_value[motor]
          elif speed < 0:
               direction = -1 * self.cali_dir_value[motor]
          speed = abs(speed)
          speed = speed - self.cali_speed_value[motor]
          if direction < 0:
               self.motor_direction_pins[motor].high()
               self.motor_speed_pins[motor].pulse_width_percent(speed)
          else:
               self.motor_direction_pins[motor].low()
               self.motor_speed_pins[motor].pulse_width_percent(speed)

     @log_on_start(logging.DEBUG , "motor_speed_calibration started {value:f}")
     @log_on_error(logging.DEBUG , "motor_speed_calibration error")
     @log_on_end(logging.DEBUG , "motor_speed_calibration endded")
     def motor_speed_calibration(self, value):
          logging.debug('calibrating speed with value: %s', value)
          self.cali_speed_value = value
          if value < 0:
               self.cali_speed_value[0] = 0
               self.cali_speed_value[1] = abs(cali_speed_value)
          else:
               self.cali_speed_value[0] = abs(cali_speed_value)
               self.cali_speed_value[1] = 0

     @log_on_start(logging.DEBUG , "motor_direction_calibration started, motor: {motor:f}, value: {value:f}")
     @log_on_error(logging.DEBUG , "motor_direction_calibration error")
     @log_on_end(logging.DEBUG , "motor_direction_calibration endded")
     def motor_direction_calibration(self, motor, value):
          # 0: positive direction
          # 1:negative direction
          logging.debug('calibrating motor direction motor: %s, value: %s', motor, value)
          motor -= 1
          if value == 1:
               self.cali_dir_value[motor] = -1*self.cali_dir_value[motor]

     @log_on_start(logging.DEBUG , "dir_servo_angle_calibration, value: {value:f}")
     @log_on_error(logging.DEBUG , "dir_servo_angle_calibration error")
     @log_on_end(logging.DEBUG , "dir_servo_angle_calibration endded")
     def dir_servo_angle_calibration(self, value):
          logging.debug('dir servo angle calibration: %s', value)
          self.dir_cal_value = value
          self.set_dir_servo_angle(self.dir_cal_value)
          # dir_servo_pin.angle(dir_cal_value)

     @log_on_start(logging.DEBUG , "set_dir_servo_angle, value: {value:f}")
     @log_on_error(logging.DEBUG , "set_dir_servo_angle error")
     @log_on_end(logging.DEBUG , "set_dir_servo_angle endded")
     def set_dir_servo_angle(self, value):
          logging.debug('set dir servo angle %s', value)
          self.steering_angle = value
          self.dir_servo_pin.angle(self.steering_angle+self.dir_cal_value)

     @log_on_start(logging.DEBUG , "camera_servo1_angle_calibration, value: {value:f}")
     @log_on_error(logging.DEBUG , "camera_servo1_angle_calibration")
     @log_on_end(logging.DEBUG , "camera_servo1_angle_calibration ended")
     def camera_servo1_angle_calibration(self, value):
          logging.debug('camera servo1 angle calibration %s', value)
          self.cam_cal_value_1 = value
          set_camera_servo1_angle(self.cam_cal_value_1)
          # camera_servo_pin1.angle(cam_cal_value)

     @log_on_start(logging.DEBUG , "camera_servo2_angle_calibration, value: {value:f}")
     @log_on_error(logging.DEBUG , "camera_servo2_angle_calibration error")
     @log_on_end(logging.DEBUG , "camera_servo2_angle_calibration ended")
     def camera_servo2_angle_calibration(self, value):
          logging.debug('camera servo2 angle calibration %s', value)
          self.cam_cal_value_2 = value
          self.set_camera_servo2_angle(self.cam_cal_value_2)
          # camera_servo_pin2.angle(cam_cal_value)

     @log_on_start(logging.DEBUG , "set_camera_servo1_angle, value: {value:f}")
     @log_on_error(logging.DEBUG , "set_camera_servo1_angle error")
     @log_on_end(logging.DEBUG , "set_camera_servo1_angle ended")
     def set_camera_servo1_angle(self, value):
          logging.debug('setting camera servo1 angle %s', value)
          self.camera_servo_pin1.angle(-1 *(value+self.cam_cal_value_1))

     @log_on_start(logging.DEBUG , "camera_servo2_angle, value: {value:f}")
     @log_on_error(logging.DEBUG , "camera_servo2_angle error")
     @log_on_end(logging.DEBUG , "camera_servo2_angle ended")
     def set_camera_servo2_angle(self, value):
          logging.debug('setting camera servo2 angle %s', value)
          camera_servo_pin2.angle(-1 * (value+self.cam_cal_value_2))

     @log_on_start(logging.DEBUG , "set_power, value: {speed:f}")
     @log_on_error(logging.DEBUG , "set_power error")
     @log_on_end(logging.DEBUG , "set_power ended")
     def set_power(self, speed):
          logging.debug('set motor power %s', speed)
          self.set_motor_speed(1, speed)
          self.set_motor_speed(2, speed) 

     @log_on_start(logging.DEBUG , "backward, value: {speed:f}")
     @log_on_error(logging.DEBUG , "backward error")
     @log_on_end(logging.DEBUG , "backward ended")

     def backward(self, speed):
          half_wheel_width = 4.75
          wheel_length = 3.75

          logging.debug('set motor speed backward %f with angle %f' , speed, self.steering_angle)

          if self.steering_angle < 0:
               # left motor moves slower than right motor
               left_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)))/(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)
               right_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)/(wheel_length/tan(abs(self.steering_angle)))

               # if greater than 100, scale faster motor to 100 and scale slower motor same ammount
               if right_motor_speed > 100:
                    scale = 100/right_motor_speed
                    right_motor_speed = scale*right_motor_speed
                    left_motor_speed = scale*left_motor_speed 
                    
          elif self.steering_angle > 0:

               # right motor moves slower than left
               right_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)))/(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)
               left_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)/(wheel_length/tan(abs(self.steering_angle)))
                    
                    # if greater than
               if left_motor_speed > 100:
                    scale = 100/left_motor_speed
                    right_motor_speed = scale*right_motor_speed
                    left_motor_speed = scale*left_motor_speed 
          else:
               if speed >100:
                    speed = 100
               right_motor_speed = speed
               left_motor_speed = speed
               
          self.set_motor_speed(1, right_motor_speed)
          self.set_motor_speed(2, left_motor_speed)

     @log_on_start(logging.DEBUG , "forward, speed value: {speed:f}")
     @log_on_error(logging.DEBUG , "forward error")
     @log_on_end(logging.DEBUG , "forward ended")
     def forward(self, speed):

          half_wheel_width = 4.75
          wheel_length = 3.75 
          logging.debug("set motor speed forward %f with angle %f", speed, self.steering_angle)

          if self.steering_angle < 0:
               # left motor moves slower than right motor
               left_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)))/(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)
               right_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)/(wheel_length/tan(abs(self.steering_angle)))

               # if greater than 100, scale faster motor to 100 and scale slower motor same ammount
               if right_motor_speed > 100:
                    scale = 100/right_motor_speed
                    right_motor_speed = scale*right_motor_speed
                    left_motor_speed = scale*left_motor_speed 
                    
          elif self.steering_angle > 0:

               # right motor moves slower than left
               right_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)))/(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)
               left_motor_speed = speed*(wheel_length/tan(abs(self.steering_angle)) + half_wheel_width)/(wheel_length/tan(abs(self.steering_angle)))
                    
                    # if greater than
               if left_motor_speed > 100:
                    scale = 100/left_motor_speed
                    right_motor_speed = scale*right_motor_speed
                    left_motor_speed = scale*left_motor_speed 
          else:
               if speed > 100:
                    speed = 100
               right_motor_speed = speed
               left_motor_speed = speed

          self.set_motor_speed(1, -1*right_motor_speed)
          self.set_motor_speed(2, -1*left_motor_speed)


     @log_on_start(logging.DEBUG , "stop")
     @log_on_error(logging.DEBUG , "stop error")
     @log_on_end(logging.DEBUG , "stop ended")
     def stop(self):
          logging.debug('stopping motors')
          self.set_motor_speed(1, 0)
          self.set_motor_speed(2, 0)

     def cleanup(self):
          self.stop()
     

