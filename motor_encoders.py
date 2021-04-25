
import RPi.GPIO as GPIO

class MotorEncoders:

     def __init__(self, left_pin, right_pin, speed_update_period):
          self.left_tick = 0
          self.right_tick = 0

          self.left_encoder_pin = Pin(left_pin)
          self.right_encoder_pin = Pin(right_pin)

          self.left_encoder_pin.irq(self.update_left_ticks, GPIO.BOTH, 1)
          self.right_encoder_pin.irq(self.update_right_ticks, GPIO.BOTH,1)

     def get_ticks(self):
          return [self.left_tick, self.right_tick]

     def update_left_ticks(self, channel):
          self.left_tick = self.left_tick + 1

     def update_right_ticks(self, channel):
          self.right_tick = self.right_tick + 1
