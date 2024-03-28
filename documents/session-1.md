# Socket programming

### create a server_socket
server_socket: specify internet protocol and communication protocol

(IP version _ transmission type): 
1. IPv4: AF_INET
2. TCP: SOCK_STREAM
3. UDP: SOCK_DGRAM

### Specify IP address and PORT number

NOTE: IP address might change on server, use take system IP address dynamically

```
import socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("host name: " + host_name + "\n" + "host ip: " + host_ip)
```
##
### Bind IP and PORT for server_socket

```
# server.py
server_ip = socket.gethostbyname(socket.gethostname())
port = 1234    # choose a random port number
server_socket.bind((server_ip, port_number))
```

NOTE: check if *PORT* number is not bind by any other process

#### check if *PORT* number is not bind by any other process
<!-- if case code to check this part automatically -->
> Windows -> powershell -> netstat -ano | select-string <port_number> 

> Linux -> terminal -> netstat -tulpn | grep <port_number>

### Put the server_socket in listening mode for any possible connection

```
# server.py
server_socket.listen()
```

### Server listen for ever to accept any connection

```
# server.py
while True:
    client_socket, client address = server_socket.accept()
```

### Send message to client
```
# server.py
while True:
    client_socket, client address = server_socket.accept()

    client_socket.send("Welcome!".encode("utf-8")) # encode the message
```

### Setup client socket 
connect client socket to server IP and PORT

```
# client.py
ip_address = <server_ip_address>
port_number = <server_port_number>
client_socket.connect((ip_address, port_number))
```

### Receive message from server
```
# client.py
msg = client_socket.recv(1024) # 1024: max Bytes client receives
print(msg.decode('utf-8')) # decode the message
```

### close the connection
> server.py --> server_socket.close()

> client.py --> client_socket.close()

## Complete code *session 1*
### server.py 
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
##
### client.py
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
##





