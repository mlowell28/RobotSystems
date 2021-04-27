import sys
import time
from picarx_improved import *
from sensors import LineSensor


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

    def interpreter_thread(self, time_delay, sensor_bus, interpreter_bus):

        self.run_thread = True
        self.time_delay = time_delay
        self.sensor_bus = sensor_bus
        self.interpreter_bus = interpreter_bus
        print("starting interpreter thread")
        while(self.run_thread):
             sensor_values = self.sensor_bus.read()
             interpreted_values = self.interpret_line_sensor(sensor_values)
             #print("interpreted values " + str(interpreted_values))
             self.interpreter_bus.write(interpreted_values)
             time.sleep(self.time_delay)

    def stop_interpreter_thread(self):
        self.run_thread = False

        
if __name__ == "__main__":
    linesensor = LineSensor()
    set_dir_servo_angle(0)
    time.sleep(5)
    interpreter = Interpreter(.002, "dark")
    set_dir_servo_angle(0)
    angle_buffer = [0]
    buffer_index = 0

    while True:
        values = linesensor.read_values()
        interpreter_output = interpreter.interpret_line_sensor(values)
       # print("Values :" + str(values))
       # print("Direction :" + str(interpreter_output))
        angle_buffer[buffer_index] = 40*interpreter_output
        #print(angle_buffer)
        buffer_index += 1
        if buffer_index == len(angle_buffer):
             buffer_index = 0
        angle_avg = sum(angle_buffer)/len(angle_buffer)
        
        #print("Angle avg: "+str(angle_avg))
        set_dir_servo_angle(angle_avg)
        forward(25)
        time.sleep(.05)
