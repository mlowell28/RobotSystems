import motor_controller
import sensors
import interpreter
import time

class Line_Follower_Controller:

     def __init__(self, scale = 40):
          self.scale = scale
          self.my_motor_controller = motor_controller.MotorController()
          self.buffer_index = 0
          self.angle_buffer = [0,0,0]

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



if __name__ == "__main__":
    linesensor = sensors.LineSensor()
    interpreter = interpreter.Interpreter(.002, "dark")
    line_follow_controller = Line_Follower_Controller()
    my_motor_controller = motor_controller.MotorController()

    while True:
        values = linesensor.read_values()
        interpreter_output = interpreter.interpret_line_sensor(values)
        angle = line_follow_controller.get_angle(interpreter_output)
        my_motor_controller.forward(30, angle)
        time.sleep(.01)
      
