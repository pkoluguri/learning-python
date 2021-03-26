import socket
import threading
import json

clients = []
ips = []

def broadcast(message,idx_c):
   for idx,client in enumerate(clients):
       if idx != idx_c:
           client.sendall(message) 

def handle_client(conn:socket.socket):
      while True:
          message = conn.recv(1024)
          broadcast(message,clients.index(conn))




if __name__ == "__main__":
    while True:
     with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind(('',48129))
        server.listen()
        conn,addr = server.accept()
        print('connected by ',addr)
        ip,port = addr 
        ips.append(ip)
        clients.append(conn)
        thread = threading.Thread(target=handle_client,args=[conn,])
        thread.start()