import socket
server_port = 21060

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1', server_port))
print('Server started')
while True:
    message, address = server_socket.recvfrom(65535)
    modified_message = str(len(str(message).split(",")))
    print('SERVER: {}'.format(modified_message))
    server_socket.sendto(bytes('Server is sending {}'.format(modified_message),encoding = 'utf8'), address)

server_socket.close()
    
