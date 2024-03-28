import socket
import threading

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

clients = []
usernames = {}

def handle_client(client_socket, address):
  """
  Handles a connected client, receiving and broadcasting messages.

  Args:
      client_socket: The socket object for the connected client.
      address: The address of the connected client.
  """
  print(f"Connected by {address}")
  username = client_socket.recv(1024).decode('utf-8')
  usernames[client_socket] = username
  broadcast(f"{username} has joined the chat!".encode('utf-8'))

  while True:
    try:
      message = client_socket.recv(1024).decode('utf-8')
      if message:
        broadcast(f"{usernames[client_socket]}: {message}".encode('utf-8'))
      else:
        remove_client(client_socket)
        break
    except:
      remove_client(client_socket)
      break

def broadcast(message):
  """
  Broadcasts a message to all connected clients.

  Args:
      message: The message to broadcast (bytes).
  """
  for client in clients:
    try:
      client.send(message)
    except:
      remove_client(client)

def remove_client(client_socket):
  """
  Removes a disconnected client from the list and broadcasts a message.

  Args:
      client_socket: The socket object of the disconnected client.
  """
  clients.remove(client_socket)
  username = usernames.pop(client_socket)
  broadcast(f"{username} has left the chat!".encode('utf-8'))
  client_socket.close()
  print(f"Client disconnected: {address}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  print(f"Server listening on {HOST}:{PORT}")
  while True:
    client_socket, address = s.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, address))
    thread.start()
