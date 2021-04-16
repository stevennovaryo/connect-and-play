import pygame
import threading
import time
from client import socketClient

server_address = input('Enter socket server address: ')
server_port = int(input('Enter socket server port: '))
password = input('Enter password: ')

socket_client = socketClient(server_address, server_port, password)

def send_key(key, status):
  start_time = time.perf_counter()
  key = key.upper()
  message = f'{key}${status}'
  socket_client.send(message)
  print(f'{message} -> {int((time.perf_counter() - start_time) * 1000)} ms')

def init():
  pygame.init()
  screen = pygame.display.set_mode((180,180))

  running = True

  while running:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        send_key(pygame.key.name(event.key), 1)
      
      if event.type == pygame.KEYUP:
        send_key(pygame.key.name(event.key), 0)

        if event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
          running = False
          socket_client.disconnect()


if __name__=="__main__":
  init()