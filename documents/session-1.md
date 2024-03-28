# Socket programming

### create a server_socket
To create a server socket, you need to specify the internet protocol (IP) version and the communication protocol. In Python, you can use the socket module to create sockets. Here are the commonly used parameters for creating a server socket:

IP version: AF_INET for IPv4
Transmission type: SOCK_STREAM for TCP, SOCK_DGRAM for UDP
```
import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Specify IP address and PORT number
To specify the IP address and port number for the server socket, you can use the bind() method. The IP address can be dynamically obtained using the gethostbyname() method. Here's an example:

file: server.py
```
import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the host IP address dynamically
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Host name: " + host_name + "\nHost IP: " + host_ip)

# Specify the IP address and port number
port = 1234    # Choose a random port number
server_socket.bind((host_ip, port))
```

#### Make sure that the port number you choose is not already bound by any other process on your system.
<!-- if case code to check this part automatically -->
> Windows -> powershell -> netstat -ano | select-string <port_number> 

> Linux -> terminal -> netstat -tulpn | grep <port_number>

### Putting the Server Socket in Listening Mode
Before accepting connections from clients, you need to put the server socket in listening mode. You can use the listen() method for this purpose.

```
# server.py
server_socket.listen()
```

### Accepting Client Connections
To accept client connections, you can use the accept() method. It returns a client socket object and the client's address. You can use the client socket object to send and receive data with the client.

```
# server.py
while True:
    client_socket, client address = server_socket.accept()
```

### Send messages to client
Once a client connection is established, you can send messages to the client using the client socket. Messages are typically encoded before sending and decoded on the receiving end.

```
# server.py
while True:
    client_socket, client address = server_socket.accept()

    client_socket.send("Welcome!".encode("utf-8")) # encode the message
```

### Setting Up the Client Socket
To connect the client socket to the server IP address and port number, you can use the connect() method.

```
# client.py
ip_address = <server_ip_address>
port_number = <server_port_number>
client_socket.connect((ip_address, port_number))
```

### Receiving Messages from the Server
To receive messages from the server, you can use the recv() method on the client socket. The method takes the maximum number of bytes to receive as an argument. The received message is typically decoded before using it.

```
# client.py
msg = client_socket.recv(1024) # 1024: max Bytes client receives
print(msg.decode('utf-8')) # decode the message
```

### Closing the Connection
To close the connection, you can use the close() method on the server socket or client socket.

> server.py --> server_socket.close()

> client.py --> client_socket.close()

## Example code *server* in python

```
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
```

## Example code *client* in python

```
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
```
