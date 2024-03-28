import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))

  # Get username from user input
  username = input("Enter your username: ")
  s.sendall(username.encode('utf-8'))

  print(f"Connected to server as {username}")
  while True:
    message = input("$")
    if message:
      s.sendall(message.encode('utf-8'))
    else:
      break

  print("Disconnected from server")
