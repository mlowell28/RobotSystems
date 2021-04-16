import sys
import time
from picarx_improved import *
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
    set_dir_servo_angle(0);
    time.sleep(10)
    linesensor = LineSensor()
    interpreter = Interpreter(.005, "dark")

    while True:
        values = linesensor.read_values()
        interpreter_output = interpreter.interpret_line_sensor(values)
        #print("Values :" + str(values))
        #print("Direction :" + str(interpreter_output))
        time.sleep(.5)
        angle = 30*interpreter_output
        set_dir_servo_angle(angle)
        forward(30)
