import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
IP = ""
ADDR = (IP,PORT)
DISCONNECT_MESSAGE = "!C!"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn , addr):
  print(f"[new connection] {addr} connected.")
  connected = True
  while connected:
      msg_length = conn.recv(HEADER).decode(FORMAT)
      if msg_length: 
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            conn.close()
        print(f"{addr} : {msg}")
      

def start():
  server.listen()
  print(f"[listening] listening on {IP}")
  while True:
      conn , addr = server.accept()
      thread = threading.Thread(target=handle_client,args=(conn,addr))
      thread.start()
      print(f"[active connections] {threading.activeCount() - 1}")


print("[starting] server is starting....")
start()