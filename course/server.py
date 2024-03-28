import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostname()) # hostname
print(socket.gethostbyname(socket.gethostname())) # host ip address

ip = socket.gethostbyname(socket.gethostname())
port = 12000

# bind IP address and port number 
server_socket.bind((ip, port))

server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    print(client_socket,":\n",type(client_socket),"\n",client_address,":\n", type(client_address),"\n\n")

    client_socket.send("Welcome!".encode("utf-8"))
    
    server_socket.close()