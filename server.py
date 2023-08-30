

import  socket
import threading, datetime, time

server_socket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Get the hostname (your computer's name)
host = socket.gethostname()
print('host:',host)

server_socket.bind((host,9090))
server_socket.listen()

print(f'server listening! at {host}')
client_socket , client_address = server_socket.accept()

while True:
        time.sleep(2)
        try:
                client_socket.send(f'halo from server to {client_address}, Now: {datetime.datetime.utcnow()}'.encode('utf-8'))
        except:
                client_socket.close()
                client_socket , client_address = server_socket.accept()
                print(f'new client at {client_address}')


