import time
from math import *
import logging
from logdecorator import  log_on_start , log_on_end , log_on_error
import atexit

try:
    from ezblock import*
    from ezblock import __reset_mcu__
    __reset_mcu__()
    time.sleep(0.01)
except ImportError:
    print("This computer does not appear to be a PiCar-X system(/opt/ezblock is not present). Shadowing hardware calls with substitute functions")
    from sim_ezblock import *

logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format , level=logging.INFO ,datefmt ="%H:%M:%S")
logging.getLogger ().setLevel(logging.DEBUG)

PERIOD = 4095
PRESCALER = 10
TIMEOUT = 0.02

steering_angle = 0

dir_servo_pin = Servo(PWM('P2'))
camera_servo_pin1 = Servo(PWM('P0'))
camera_servo_pin2 = Servo(PWM('P1'))
left_rear_pwm_pin = PWM("P13")
right_rear_pwm_pin = PWM("P12")
left_rear_dir_pin = Pin("D4")
right_rear_dir_pin = Pin("D5")

S0 = ADC('A0')
S1 = ADC('A1')
S2 = ADC('A2')

Servo_dir_flag = 1
dir_cal_value = -5.5
cam_cal_value_1 = 0
cam_cal_value_2 = 0
motor_direction_pins = [left_rear_dir_pin, right_rear_dir_pin]
motor_speed_pins = [left_rear_pwm_pin, right_rear_pwm_pin]
cali_dir_value = [-1, 1]
cali_speed_value = [0, 0]

for pin in motor_speed_pins:
    pin.period(PERIOD)
    pin.prescaler(PRESCALER)

#@log_on_start(logging.DEBUG , "set_motor_speed started, motor: {motor:f}, speed: {speed:f}")
#@log_on_error(logging.DEBUG , "set_motor_speed  encountersan error  before  completing ")
#@log_on_end(logging.DEBUG , "set_motor_speed completed")
def set_motor_speed(motor, speed):
    logging.debug('setting motor speed, motor: %f, speed: %f', motor, speed)
    global cali_speed_value,cali_dir_value
    motor -= 1
    if speed >= 0:
        direction = 1 * cali_dir_value[motor]
    elif speed < 0:
        direction = -1 * cali_dir_value[motor]
    speed = abs(speed)
    speed = speed - cali_speed_value[motor]
    if direction < 0:
        motor_direction_pins[motor].high()
        motor_speed_pins[motor].pulse_width_percent(speed)
    else:
        motor_direction_pins[motor].low()
        motor_speed_pins[motor].pulse_width_percent(speed)

#@log_on_start(logging.DEBUG , "motor_speed_calibration started {value:f}")
#@log_on_error(logging.DEBUG , "motor_speed_calibration error")
#@log_on_end(logging.DEBUG , "motor_speed_calibration endded")
def motor_speed_calibration(value):
    logging.debug('calibrating speed with value: %s', value)
    global cali_speed_value,cali_dir_value
    cali_speed_value = value
    if value < 0:
        cali_speed_value[0] = 0
        cali_speed_value[1] = abs(cali_speed_value)
    else:
        cali_speed_value[0] = abs(cali_speed_value)
        cali_speed_value[1] = 0

#@log_on_start(logging.DEBUG , "motor_direction_calibration started, motor: {motor:f}, value: {value:f}")
#@log_on_error(logging.DEBUG , "motor_direction_calibration error")
#@log_on_end(logging.DEBUG , "motor_direction_calibration endded")
def motor_direction_calibration(motor, value):
    # 0: positive direction
    # 1:negative direction
    logging.debug('calibrating motor direction motor: %s, value: %s', motor, value)
    global cali_dir_value
    motor -= 1
    if value == 1:
        cali_dir_value[motor] = -1*cali_dir_value[motor]

#@log_on_start(logging.DEBUG , "dir_servo_angle_calibration, value: {value:f}")
#@log_on_error(logging.DEBUG , "dir_servo_angle_calibration error")
#@log_on_end(logging.DEBUG , "dir_servo_angle_calibration endded")
def dir_servo_angle_calibration(value):
    logging.debug('dir servo angle calibration: %s', value)
    global dir_cal_value
    dir_cal_value = value
    set_dir_servo_angle(dir_cal_value)
    # dir_servo_pin.angle(dir_cal_value)

#@log_on_start(logging.DEBUG , "set_dir_servo_angle, value: {value:f}")
#@log_on_error(logging.DEBUG , "set_dir_servo_angle error")
#@log_on_end(logging.DEBUG , "set_dir_servo_angle endded")
def set_dir_servo_angle(value):
    logging.debug('set dir servo angle %s', value)
    global dir_cal_value
    global steering_angle 
    steering_angle = value
    dir_servo_pin.angle(value+dir_cal_value)

#@log_on_start(logging.DEBUG , "camera_servo1_angle_calibration, value: {value:f}")
#@log_on_error(logging.DEBUG , "camera_servo1_angle_calibration")
#@log_on_end(logging.DEBUG , "camera_servo1_angle_calibration ended")
def camera_servo1_angle_calibration(value):
    logging.debug('camera servo1 angle calibration %s', value)
    global cam_cal_value_1
    cam_cal_value_1 = value
    set_camera_servo1_angle(cam_cal_value_1)
    # camera_servo_pin1.angle(cam_cal_value)

#@log_on_start(logging.DEBUG , "camera_servo2_angle_calibration, value: {value:f}")
#@log_on_error(logging.DEBUG , "camera_servo2_angle_calibration error")
#@log_on_end(logging.DEBUG , "camera_servo2_angle_calibration ended")
def camera_servo2_angle_calibration(value):
    logging.debug('camera servo2 angle calibration %s', value)
    global cam_cal_value_2
    cam_cal_value_2 = value
    set_camera_servo2_angle(cam_cal_value_2)
    # camera_servo_pin2.angle(cam_cal_value)

#@log_on_start(logging.DEBUG , "set_camera_servo1_angle, value: {value:f}")
#@log_on_error(logging.DEBUG , "set_camera_servo1_angle error")
#@log_on_end(logging.DEBUG , "set_camera_servo1_angle ended")
def set_camera_servo1_angle(value):
    logging.debug('setting camera servo1 angle %s', value)
    global cam_cal_value_1
    camera_servo_pin1.angle(-1 *(value+cam_cal_value_1))

#@log_on_start(logging.DEBUG , "camera_servo2_angle, value: {value:f}")
#@log_on_error(logging.DEBUG , "camera_servo2_angle error")
#@log_on_end(logging.DEBUG , "camera_servo2_angle ended")
def set_camera_servo2_angle(value):
    logging.debug('setting camera servo2 angle %s', value)
    global cam_cal_value_2
    camera_servo_pin2.angle(-1 * (value+cam_cal_value_2))

#@log_on_start(logging.DEBUG , "get_adc_value")
#@log_on_error(logging.DEBUG , "get_adc_value error")
#@log_on_end(logging.DEBUG , "get_adc_value ended")
def get_adc_value():
    logging.debug('getting ADC values')
    adc_value_list = []
    adc_value_list.append(S0.read())
    adc_value_list.append(S1.read())
    adc_value_list.append(S2.read())
    return adc_value_list

#@log_on_start(logging.DEBUG , "set_power, value: {speed:f}")
#@log_on_error(logging.DEBUG , "set_power error")
#@log_on_end(logging.DEBUG , "set_power ended")
def set_power(speed):
    logging.debug('set motor power %s', speed)
    set_motor_speed(1, speed)
    set_motor_speed(2, speed) 

#@log_on_start(logging.DEBUG , "backward, value: {speed:f}")
#@log_on_error(logging.DEBUG , "backward error")
#@log_on_end(logging.DEBUG , "backward ended")

def backward(speed):

    half_wheel_width = 4.75
    wheel_length = 3.75
    global steering_angle

    logging.debug('set motor speed backward %f with angle %f' , speed, steering_angle)

    if steering_angle < 0:
        # left motor moves slower than right motor
        left_motor_speed = speed*(wheel_length/tan(2*pi/360*abs(steering_angle)))/(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)
        right_motor_speed = speed*(wheel_length/tan(abs(2*pi/360*steering_angle)) + half_wheel_width)/(wheel_length/tan(2*pi/360*abs(steering_angle)))

        # if greater than 100, scale faster motor to 100 and scale slower motor same ammount
        if right_motor_speed > 100:
            scale = 100/right_motor_speed
            right_motor_speed = scale*right_motor_speed
            left_motor_speed = scale*left_motor_speed 
            
    elif steering_angle > 0:

        # right motor moves slower than left
        right_motor_speed = speed*(wheel_length/tan(2*pi/360*abs(steering_angle)))/(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)
        left_motor_speed = speed*(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)/(wheel_length/tan(2*pi/360*abs(steering_angle)))
            
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
        
    set_motor_speed(1, -1*right_motor_speed)
    set_motor_speed(2, -1*left_motor_speed)

#@log_on_start(logging.DEBUG , "forward, speed value: {speed:f}")
#@log_on_error(logging.DEBUG , "forward error")
#@log_on_end(logging.DEBUG , "forward ended")
def forward(speed):

    half_wheel_width = 4.75
    wheel_length = 3.75 
    global steering_angle 

    logging.debug("set motor speed forward %f with angle %f", speed, steering_angle)

    if steering_angle < 0:
        # left motor moves slower than right motor
        left_motor_speed = speed*(wheel_length/tan(2*pi/360 * abs(steering_angle)))/(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)
        right_motor_speed = speed*(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)/(wheel_length/tan(2*pi/360*abs(steering_angle)))

        print("left motor speed: " + str(left_motor_speed))
        print("right motor speed " + str(right_motor_speed)) 

        # if greater than 100, scale faster motor to 100 and scale slower motor same ammount
        if right_motor_speed > 100:
            scale = 100/right_motor_speed
            right_motor_speed = scale*right_motor_speed
            left_motor_speed = scale*left_motor_speed 
            
    elif steering_angle > 0:

        # right motor moves slower than left
        right_motor_speed = speed*(wheel_length/tan(2*pi/360*abs(steering_angle)))/(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)
        left_motor_speed = speed*(wheel_length/tan(2*pi/360*abs(steering_angle)) + half_wheel_width)/(wheel_length/tan(2*pi/360*abs(steering_angle)))
            
        print("left motor speed: " + str(left_motor_speed))
        print("right motor speed: " + str(right_motor_speed))
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

    set_motor_speed(1, right_motor_speed)
    set_motor_speed(2, left_motor_speed)


#@log_on_start(logging.DEBUG , "stop")
#@log_on_error(logging.DEBUG , "stop error")
#@log_on_end(logging.DEBUG , "stop ended")
def stop():
    logging.debug('stopping motors')
    set_motor_speed(1, 0)
    set_motor_speed(2, 0)

#@log_on_start(logging.DEBUG , "Get_distance")
#@log_on_error(logging.DEBUG , "Get_distance error")
#@log_on_end(logging.DEBUG , "Get_distance ended")
def Get_distance():
    logging.debug('measuring distance')
    timeout=0.01
    trig = Pin('D8')
    echo = Pin('D9')

    trig.low()
    time.sleep(0.01)
    trig.high()
    time.sleep(0.000015)
    trig.low()
    pulse_end = 0
    pulse_start = 0
    timeout_start = time.time()
    while echo.value()==0:
        pulse_start = time.time()
        if pulse_start - timeout_start > timeout:
            return -1
    while echo.value()==1:
        pulse_end = time.time()
        if pulse_end - timeout_start > timeout:
            return -2
    during = pulse_end - pulse_start
    cm = round(during * 340 / 2 * 100, 2)
    #print(cm)
    return cm
     
def test():
    
    angles = [-30, -20, -10, 0, 10, 20, 30]    

    for angle in angles:
         print("angle " + str(angle))
         set_dir_servo_angle(angle)
         forward(50)
         time.sleep(5)

    for angle in angles:
         print("angle " + str(angle))
         set_dir_servo_angle(angle)
         backward(50)
         time.sleep(5)
 

#force stop function to run at exit of script which includes picarx_improved
atexit.register(stop)

if __name__ == "__main__":
    while(1):
        test()
