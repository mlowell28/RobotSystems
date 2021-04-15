import sys
import time
from sensors import *

class Interpreter:
    def __init__(self, sensitivity = 1, follow_type = "light"):   

        self.sensitivity = sensitivity
        self.polarity = follow_type

    def interpret_line_sensor(self, values):
        sensor_values = values
        if self.polarity == "light":
            output = self.sensitivity*(sensor_values[1]-sensor_values[0] - (sensor_values[1]-sensor_values[2]))
        elif self.polarity == "dark":
            output = -1*self.sensitivity*(sensor_values[1]-sensor_values[0] - (sensor_values[1]-sensor_values[2]))
        
        if abs(output) > 1:
            output = output/abs(output)
        return output


        
if __name__ == "__main__":
    linesensor = LineSensor(.001)
    interpreter = Interpreter(100, "light")

    while True:
        values = linesensor.read_values()
        interpreter_output = interpreter.(values)
        print("Values :" + str(values))
        print("Direction :" + str(interpreter_output))
        time.sleep(.1)
        set_dir_servo_angle(20*direction)