import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

messag_length = 100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysocket:
    mysocket.bind((HOST, PORT))
    mysocket.listen()
    conn, addr = mysocket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            buffer = conn.recv(message_length)
            message = buffer
            if len(command) < message_length:
                buffer = conn.recv(message_length-len(message))
                if buffer == 0:
                    mysocket.shutdown()
                    mysocket.close()
                message = [message, buffer]
            print("message")
                
                 
            #if not command:
             #   break
            #conn.sendall(data)
