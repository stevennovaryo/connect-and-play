import socket

class socketClient:
  FORMAT = 'utf-8'
  DISCONNECT_MESSAGE = 'DC'

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  def __init__(self, server_address, port, password):
    self.SERVER = server_address
    self.PORT = port
    self.ADDR = (self.SERVER, self.PORT)
    self.client.connect(self.ADDR)
    self.PASSWORD = password
    
  
  def send(self, raw_msg):
    message = f'{self.PASSWORD} {raw_msg}'.encode(self.FORMAT)
    message += b' ' * (256 - len(message))

    self.client.send(message)

  def disconnect(self):
    self.send(self.DISCONNECT_MESSAGE)