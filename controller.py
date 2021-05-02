import motor_controller
import sensors
import interpreter
import time
import bus
import concurrent.futures
import atexit

class Line_Follower_Controller:

     def __init__(self, scale = 40, speed = 50):
          self.scale = scale
          self.my_motor_controller = motor_controller.MotorController(use_PID = True)
          self.buffer_index = 0
          self.angle_buffer = [0,0,0]
          self.speed = speed
          print("Line Follower init run")

     def get_angle(self, interpreter_output): 
          self.angle_buffer[self.buffer_index] = self.scale*interpreter_output
          self.buffer_index += 1
          if self.buffer_index == len(self.angle_buffer):
               self.buffer_index = 0
          self.angle_avg = sum(self.angle_buffer)/len(self.angle_buffer)
          self.my_motor_controller.set_dir_servo_angle(self.angle_avg)
          return self.angle_avg

     def set_scale(self,scale):
          self.scale = scale

     def line_follower_controller_thread(self, time_delay, interpreter_bus, ultrasonic_sensor_bus):
          
          print("starting line follower loop")
          self.run_thread = True
          self.interpreter_bus = interpreter_bus
          self.time_delay = time_delay
           
          while(self.run_thread):
               ultrasonic_distance = self.ultrasonic_sensor_bus.read()
               if distance < 10:
                    continue 
               interpreter_output = self.interpreter_bus.read()
               angle = self.get_angle(interpreter_output)
               #print("setting angle "+str(angle))
               self.my_motor_controller.set_dir_servo_angle(angle)
               #print("setting forward speed " +  str(self.speed))
               self.my_motor_controller.forward(self.speed)
               time.sleep(time_delay)

     def stop_sensor_thread(self):
          self.run_thread = False


if __name__ == "__main__":
    
    line_sensor_delay = .01
    line_sensor_bus = bus.bus()
    
    ultrasonic_sensor_delay = 1
    ultrasonic_sensor_bus = bus.bus()

    interpreter_delay = .01
    interpreter_bus = bus.bus(0)

    controller_delay = .1
    
    linesensor = sensors.LineSensor()
    ultrasonicsensor = sensors.UltrasonicSensor()

    interpreter = interpreter.Interpreter(.002, "dark")
    line_follower_controller = Line_Follower_Controller()
    print("starting threads")
    with  concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
         line_sensor_executor = executor.submit(linesensor.sensor_thread, line_sensor_delay, line_sensor_bus)
         ultrasonic_sensor_exectuor = executor.submit(ultrasonicsensor.ultraonisc_sensor_thread, utrasonic_sensor_delay, ultrasonic_sensor_bus 
         interpreter_executor = executor.submit(interpreter.interpreter_thread, interpreter_delay, sensor_bus, interpreter_bus)
         line_follower_executor = executor.submit(line_follower_controller.line_follower_controller_thread, controller_delay, interpreter_bus)

