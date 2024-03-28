import socket

# create a client side IPv4 socket and TCP connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server
ip_address = socket.gethostbyname(socket.gethostname())
port = 12000

print(ip_address)

client_socket.connect((ip_address, port))

msg = client_socket.recv(1024)
print(msg.decode("utf-8"))

client_socket.close()