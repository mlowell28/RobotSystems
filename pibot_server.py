

import socket
import struct
import time
import threading
import bus
from picamera import PiCamera
import io

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
            payload_size = struct.unpack('<i', header)
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
        

def send(conn, command_bus = None):
    
    camera = picamera.PiCamera()
    camera.resolution(640,480)
    camera.start_preview()
    time.sleep(2)

    socket_file = conn.make_file('wb')
    stream = io.BytesIO()
    
    while(continue_send == True):
        for picture in camera.capture_continuous(stream, 'jpeg'):
    
            # read currently running command
            command = command_bus.read()
            encoded_command = command.encode('utf-8')
            command_length = len(encoded_command)
    
            # pack command via 4 by header giving length infront of byte encoded command
            command_header = struct.pack('<i', command_length)
            socket_file.write(command_header)
            socket_file.write(encoded_command)
    
            #pack byte size of image
            image_header = struct.pack('<i', stream.tell())
            socket_file.write(image_header)
            
            # reset stream position to 0
            stream.seek(0)
    
            # send data
            socket_file.write(stream.read())
            socket_file.flush()
    
            # reset stream
            stream.seek(0)
            stream.truncate()
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
    
    print("starting pibot server")
    HOST = socket.gethostbyname("pibot.local")
    print("Listening on address:" + str(HOST) + " port: "+ str(PORT))
    mysocket.bind((HOST, PORT))
    mysocket.listen()
    while(1):
        conn, addr = mysocket.accept()
        with conn:
            print('Connected by', addr)
            command_bus = bus.bus()
            continue_recv = True
            
            print("starting command receive thread")
            recv_thread = threading.Thread(target=recv, args=(conn, command_bus))
            recv_thread.start()
            
            continue_send = True
            print("starting image sending thread")
            send_thread = threading.Thread(target=send, args=(conn,))
            send_thread.start()
            
            print("starting control loop")
            done = False

            while done == False:
                message = command_bus.read_clear()

                if message != None:

                    chunks = message.split(' ')

                    print("Command Received is: "+ message)

                    if chunks[0]== "send_data":
                        continue_tranmission = True
                        transmitter_thread = threading.Thread(target=send,args=(conn,))
                        transmitter_thread.start()

                    if chunks[0] == "stop_sending":
                        continue_tranmission = False
                    
                    if chunks[0] == "quit":
                        continue_recv = False
                        continue_tranmission = False
                        done = True
                    
                    if chunks[0] == "forward":
                        print("setting forward as " + str(chunks[1]))
                        print("setting angle as " + str(chunks[3]))

                    if chunks[0] == "backward":
                        print("setting backward as " + str(chunks[1]))
                        print("setting angle as " + str(chunks[3]))
    
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

#def data_recv_thread(conn):

