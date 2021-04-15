
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from ezblock import ADC
from ezblock import print

my_3ch = None

adc_A0=ADC("A0")
adc_A1=ADC("A1")
adc_A2=ADC("A2")



class LineSensor:
    def __init__(self, sensitivity = 1, follow_type = "light"):   

        self.sensitivity = sensitivity
        self.polarity = follow_type
        self.sensor_values = [0,0,0]

    def read_values(self):
        sensor_values = [adc_A0.read(), adc_A1.read(), adc_A2.read()]
        self.sensor_values = sensor_values
        return sensor_values

    def get_saved_values(self):
        return self.sensor_values 

    def get_direction(self):
        sensor_values = self.read_values()
        if self.polarity == "light":
            output = self.sensitivity*(sensor_values[1]-sensor_values[0] - (sensor_values[1]-sensor_values[2]))
        elif self.polarity == "dark":
            output = -1*self.sensitivity*(sensor_values[1]-sensor_values[0] - (sensor_values[1]-sensor_values[2]))
        
        if abs(output) > 1:
            output = output/abs(output)
        return output


        
if __name__ == "__main__":
    linesensor = LineSensor()
    while True:
        values = linesensor.read_values()
        direction = linesensor.get_direction()
        print("Values :" + str(values))
        print("Direction :" + str(direction))
        time.sleep(1)

    
        

        



