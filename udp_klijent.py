import socket
import time
start = time.time()
time.sleep(8)
server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input_s = 'Crvena, zvezda!'
client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
input_s_modified, address = client_socket.recvfrom(65535)
print ('[CLIENT] Response from server {}, is: "{}"'.format(address, str(input_s_modified.decode('utf8'))))
kraj = time.time()
razlika = kraj - start
print(razlika)
client_socket.close()
