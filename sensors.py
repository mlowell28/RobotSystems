
import sys
import copy
sys.path.append(r'/opt/ezblock')
import time
from ezblock import Ultrasonic
from ezblock import ADC
from ezblock import Pin
adc_A0=ADC("A0")
adc_A1=ADC("A1")
adc_A2=ADC("A2")

class LineSensor:
    def __init__(self):   

        self.sensor_values = [0,0,0]
        self.run_thread = None

    def read_values(self):
        sensor_values = [adc_A0.read(), adc_A1.read(), adc_A2.read()]
        self.sensor_values = sensor_values
        return sensor_values

    def get_saved_values(self):
        return self.sensor_values 

    def line_sensor_thread(self, time_delay, sensor_bus):
        self.run_thread = True
        self.time_delay = time_delay
        self.sensor_bus = sensor_bus
        print("starting line sensor thread")
        while self.run_thread:
            values = self.read_values()
            self.sensor_bus.write(copy.deepcopy(values))
            time.sleep(self.time_delay)

    def stop_line_sensor_thread(self):
        self.run_thread = False

class UltrasonicSensor:
    def __init__(self):
        self.distance = 0
    
    def read_distance(self):
        return self.distance

    def get_saved_distance(self):
        return self.distance

    def ultrasonic_sensor_thread(self, time_delay, sensor_bus):
        self.run_thread = True
        self.time_delay = time_delay
        self.sensor_bus = sensor_bus
        pin_D0=Pin("D0")
        pin_D1=Pin("D1")
        print("Starting ultrasonic sensor thread")

        while(self.run_thread == True):
            self.distance = Ultrasonic(pin_D0, pin_D1).read()
            sensor_bus.write(self.distance)
            time.sleep(self.time_delay)
            

    def stop_ultrasonic_sensor_thread(self):
        self.run_thread = False

        
if __name__ == "__main__":
    linesensor = LineSensor()
    while True:
        values = linesensor.read_values()
        print("Values :" + str(values))
        time.sleep(.1)

    
        

        



