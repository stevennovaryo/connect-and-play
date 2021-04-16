import socket
import threading
from utils import input_processor

class Server:
  HEADER = 64
  PORT = 5050
  SERVER = '127.0.0.1'
  ADDR = (SERVER, PORT)
  FORMAT = 'utf-8'
  DISCONNECT_MESSAGE = 'DC'

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(ADDR)

  def __init__(self, **kwargs):
    self.PORT = kwargs.get('PORT', 5050)
    self.SERVER = kwargs.get('SERVER', '127.0.0.1')
    self.ADDR = (self.SERVER, self.PORT)
    self.PASSWORD = kwargs.get('PASSWORD')

  def get_client_message(self, conn, length):
    message = conn.recv(length).decode(self.FORMAT)
  
    password, message = message.split()
    assert(password == self.PASSWORD)
    return message

  def handle_client(self, conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
  
    connected = True
    while connected:
      try:
        message = self.get_client_message(conn, 256)
      except:
        continue
    
      if message == self.DISCONNECT_MESSAGE:
        connected = False
    
      print(f'[{addr}] {message}')
      input_processor.process_input(message)

  def start(self):
    self.server.listen()
    print(f'[LISTENING] Server is listening on {self.SERVER}:{self.PORT}.')
    while True:
      conn, addr = self.server.accept()
      thread = threading.Thread(target=self.handle_client, args=(conn, addr))
      thread.start()
      print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')