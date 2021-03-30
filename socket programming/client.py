import socket
import threading

FORMAT = "utf-8"
IP = "192.168.29.167"
PORT = 21233
nickname = ""
HEADER = 60
ADDR = (IP,PORT)
DISCONNECT_MESSAGE = "!close!"
clients = []

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
     client.send(msg.encode(FORMAT))

def recv_msg():
     while True:
          msg = client.recv(1024).decode(FORMAT).strip('\n')
          if len(msg) > 0 and repr(msg) != "\n":
           print("\n"+msg+"\n")
           print("enter the message:")

def send_msg():
     while True:
          msg = input("enter the message:\n")
          if msg != "" and msg != " ":
           send(nickname+":"+msg)

if __name__ == "__main__":
     nickname = input("enter your nickname:")
     send(nickname)
     no_of_messages = int(client.recv(1024).decode(FORMAT))
     if no_of_messages > 0:
      for _ in range(no_of_messages):
          msg = client.recv(1024).decode(FORMAT)
          print("\n"+msg+"\n")

     thread = threading.Thread(target=recv_msg)
     thread2 = threading.Thread(target=send_msg)
     thread.start()
     thread2.start()