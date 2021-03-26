import socket

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
IP = "49.37.156.73"
ADDR = (IP,PORT)
DISCONNECT_MESSAGE = "!C!"
ADDR = (IP,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

while True:
 msg = str(input(">"))
 send(msg)