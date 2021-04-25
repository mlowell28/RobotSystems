import socket
import struct
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

command_message_size = 10
image_size = 4

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
encoded_message = MESSAGE.encode('utf-8')
message_size = len(encoded_message) 

first_byte = struct.pack('i', message_size)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, PORT))

to_send = bytearray(first_byte)
to_send.append(encoded_message)

sent_length = s.send(to_send)
index = 0

while sent_length < len(to_send):
    send = s.send(to_send)
    sent_length = sent_length + send

#data = s.recv(BUFFER_SIZE)
s.close()
 
#print "received data:", data