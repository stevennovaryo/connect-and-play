import threading
from decouple import config
from utils.server import Server
from utils.key_press_sim import start_simulator

socketServer = Server(PORT=config('PORT'), PASSWORD=config('PASSWORD'))

def main():
  print('Starting socket server...')
  server_thread = threading.Thread(target=socketServer.start)
  server_thread.start()
  
  print('Starting simulator...')
  simulator_thread = threading.Thread(target=start_simulator)
  simulator_thread.start()
  

if __name__ == "__main__":
  main()