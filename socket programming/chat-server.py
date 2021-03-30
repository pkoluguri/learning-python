import socket
import threading
import time
import json

FORMAT = "utf-8"
IP = ""
PORT = 21233
HEADER = 60
ADDR = (IP,PORT)
DISCONNECT_MESSAGE = "!close!"
clients = []

def write_message(messages:list):
  jsonfilewrite = open("messages.json","w")
  json_write_format = {"messages":messages}
  json_write_format = json.dumps(json_write_format,indent=2)
  jsonfilewrite.write(json_write_format)

def read_messages():
  jsonfile = open("messages.json","r")
  json_format = jsonfile.read()
  json_read_format = json.loads(json_format)
  messages = json_read_format["messages"]
  return messages

def isfull(messages_list):
  if len(messages_list) >= 100:
    return True
  return False

def broadcast(msg,idx):
 for idxc,client in enumerate(clients):
   if idxc != idx:
       client.send(msg.encode(FORMAT))

def handle_client(conn):
    idx = clients.index(conn)
    nickname = conn.recv(1024).decode(FORMAT)
    messages = read_messages()
    conn.send(str(len(messages)).encode(FORMAT))
    time.sleep(1)
    for message in messages:
      conn.send(message.encode(FORMAT))
      time.sleep(0.1)
    msg = ""
    if nickname:
     broadcast(nickname+" has joined the server!",idx)
    while True:
      try:
       msg =conn.recv(1024).decode(FORMAT)
       if len(msg) > 4 and not isfull(messages): 
         print(len(msg))
         broadcast(msg,idx)
         messages = read_messages()
         messages.append(msg)
         write_message(messages)
       else:
         if len(msg) > 4:
           messages = read_messages()
           messages.pop(0)
           messages.append(msg) 
           write_message(messages)
      except ConnectionResetError:
        clients.remove(conn)
        conn.close()
        return
if __name__ == "__main__":
 with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
      server.bind(ADDR)
      print("listening on "+str(PORT))
      while True:
        server.listen()
        conn,addr = server.accept()
        print("connected by ",addr)
        clients.append(conn)
        thread = threading.Thread(target=handle_client,args=[conn,])
        thread.start()