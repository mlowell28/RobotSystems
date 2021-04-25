
import threading
import copy
import time


class bus():
     def __init__(self, message = None):
          self.lock = threading.Lock()
          self.message = message

     def write(self, message):
         self.lock.acquire()
         self.message = message
         self.lock.release()

     def read(self):
         self.lock.acquire()
         message = copy.deepcopy(self.message)
         self.lock.release()
         return message


 