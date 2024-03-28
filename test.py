import socket
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("host name: " + host_name + "\n" + "host ip: " + host_ip)