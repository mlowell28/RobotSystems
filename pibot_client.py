import time
import threading
import socket
import struct
import bus
import io

#SERVER = '127.0.0.1'  # Standard loopback interface address (localhost)
SERVER = "pibot.local"
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def send(conn, send_bus):
    send_data = True
    while send_data == True:
        data = send_bus.read_clear()
        if data != None:
            data_size = len(data)
            header = struct.pack('<i', data_size)
            to_send = bytearray(header)
            to_send.extend(data)

            print("sending message")
            sent_length = conn.send(to_send)
            print("sent chunk length "+ str(sent_length))

            while sent_length < len(to_send):
                send = conn.send(to_send)
                sent_length = sent_length + send
                print("sent chunk length " + str(sent_length))


def recv(conn, recv_bus):
        
        # receive command
       recv_data = True
       while recv_data == True:
            bytes_received = bytearray()
            buffer = conn.recv(4)
            bytes_received.extend(buffer)
            # header is 4 bytes long, gives byte length of rest of message
            while len(bytes_received) < 4:
                buffer = conn.recv(4-len(bytes_received))
                bytes_received.extend(buffer)
           
            print("buffer read " + str(len(buffer)))
            header = bytes_received[0:4]
            payload_size = struct.unpack('<i', header)
            payload_size  = payload_size[0]
            print("command size: " + str(payload_size))

            payload = bytearray()
            buffer = conn.recv(payload_size)

            payload.extend(buffer)
            print("command size received " + str(len(buffer)))

            while len(payload) < payload_size: 
                print("command bytes left to receive " + str(payload_size - len(payload)))
                buffer = conn.recv(payload_size - len(payload))
                print("command bytes received " + str(len(buffer)))
                payload.extend(buffer)

            message = payload.decode('utf-8')
            print("Command Received is: "+ message)

            # receive image
            bytes_received = bytearray()
            buffer = conn.recv(4)
            bytes_received.extend(buffer)
            # header is 4 bytes long, gives byte length of rest of message
            while len(bytes_received) < 4:
                buffer = conn.recv(4-len(bytes_received))
                bytes_received.extend(buffer)
           
            print("buffer read " + str(len(buffer)))
            header = bytes_received[0:4]
            payload_size = struct.unpack('i', header)
            payload_size  = payload_size[0]
            print("Image size: " + str(payload_size))

            payload = bytearray()
            buffer = conn.recv(payload_size)

            payload.extend(buffer)
            print("Image size received " + str(len(buffer)))

            while len(payload) < payload_size: 
                print("Image bytes left to receive " + str(payload_size - len(payload)))
                buffer = conn.recv(payload_size - len(payload))
                print("Image bytes received " + str(len(buffer)))
                payload.extend(buffer)
            image = payload 

            image_file = io.BytesIO(image)
            image_file.show()
            recv_bus.write([message, image])



# connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    
    print("getting pibot IP")
    address = socket.gethostbyname(SERVER)
    print("pibot IP is " + str(address))
    print("connecting to " + str(address) + " port " + str(PORT))
    conn.connect((address, PORT))
    print("connected")

    # def buses
    send_bus = bus.bus()
    recv_bus = bus.bus()

    # spin up send and receive threads
    send_thread = threading.Thread(target=send, args=(conn, send_bus))
    send_thread.start()
    recv_thread = threading.Thread(target=recv, args=(conn, recv_bus))
    recv_thread.start()

    while(1):
        
        print()
        start_send = "send_data"
        send_bus.write(start_send.encode('utf-8'))

        time.sleep(20)

        stop_send = "stop_sending_data"
        send_bus.write(stop_send.encode('utf-8'))

        time.sleep(20)

print("done")

conn.close()
time.sleep(10)
 
