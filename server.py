import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
    mysocket.bind((HOST, PORT))
    mysocket.listen()
    conn, addr = mysocket.accept()
    with conn:
        print('Connected by', addr)

        message_count = 0

        while message_count < 10:
            bytes_received = bytearray()
            buffer = conn.recv(message_length)
            bytes_received.append(buffer)
            if len(bytes_received) < 4:
                buffer = conn.recv()
                bytes_received.append(buffer)

            header = buffer[0:3]
            payload_size = struct.unpack('i', header)

            payload = buffer[4:]

            if len(payload) < payload_size: 
                buffer = conn.recv()
                payload.append(buffer)

            message = payload[4:payload_size]
            message = text.decode('utf-8')
            print(message)

            message_count +=1
    
        conn.shutdown()
        conn.close()

        receiving_commands_thread
        # control to start data transmission
        # control to end data transmission
        # control to control robot
        
        data_transmission_thread
        # capture image
        # capture current control command
        # send back


