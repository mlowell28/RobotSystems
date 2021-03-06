

import socket
import struct
import time
import threading
import bus
import picamera

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def recv(conn, command_bus):

    while(continue_recv == True):
           
            bytes_received = bytearray()
            
            #header is 4 bytes giving message length in bytes
            buffer = conn.recv(4)
            bytes_received.extend(buffer)
            # verify header is fully received
            while len(bytes_received) < 4:
                buffer = conn.recv(4-len(bytes_received))
                bytes_received.extend(buffer)
           
            print("buffer read " + str(len(buffer)))
            header = bytes_received[0:4]
            payload_size = struct.unpack('i', header)
            payload_size  = payload_size[0]
            print("payload size: " + str(payload_size))

            # message payload is payload_size bytes long
            payload = bytearray()
            buffer = conn.recv(payload_size)

            payload.extend(buffer)
            print("payload size received " + str(len(buffer)))
            # loop until full payload is received
            while len(payload) < payload_size: 
                print("payload bytes left to receive " + str(payload_size - len(payload)))
                buffer = conn.recv(payload_size - len(payload))
                print("payload bytes received " + str(len(buffer)))
                payload.extend(buffer)

            # decode
            message = payload.decode('utf-8')
            print("message received " + str(message))
            command_bus.write(message)
        

def send(conn):
    
        while(continue_tranmission == True):
            MESSAGE = "Test"
            encoded_message = MESSAGE.encode('utf-8')
            message_size = len(encoded_message) 
            header = struct.pack('i', message_size)
            to_send = bytearray(header)
            to_send.extend(encoded_message)
            print("sending message")
            sent_length = conn.send(to_send)
            print("sent chunk length "+ str(sent_length))

            while sent_length < len(to_send):
                send = conn.send(to_send)
                sent_length = sent_length + send
                print("sent chunk length " + str(sent_length))

            print("done sending message")

            time.sleep(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
    mysocket.bind((HOST, PORT))
    mysocket.listen()
    while(1):
        conn, addr = mysocket.accept()
        with conn:
            print('Connected by', addr)
            command_bus = bus.bus()
            continue_recv = True
            recv_thread = threading.Thread(target=recv, args=(conn, command_bus))
            recv_thread.start()
            done = False

            while done == False:
                message = command_bus.read_clear()

                if message != None:

                    print("Command Received is: "+ message)

                    if message == "send data":
                        continue_tranmission = True
                        transmitter_thread = threading.Thread(target=send,args=(conn,))
                        transmitter_thread.start()

                    if message == "stop sending":
                        continue_tranmission = False
                    
                    if message == "quit":
                        continue_recv = False
                        continue_tranmission = False
                        done = True


        conn.shutdown(socket.SHUT_RDWR)
        conn.close()




