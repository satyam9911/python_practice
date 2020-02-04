from socket import AF_INET,socket,SOCK_STREAM
import sys
import threading
conn = True
BUFSIZE = 1024
host = input("Enter host ip:")
port = input("Enter port number:")
ADDR = (host,int(port))
client_socket = socket(AF_INET,SOCK_STREAM)
try:
    client_socket.connect(ADDR)
except:
    print(sys.exc_info()[1])
msg = client_socket.recv(BUFSIZE).decode("utf8")
print(msg)
msg=input(">> ")
client_socket.send(bytes(msg,"utf8"))

def receive_message():
    msg = client_socket.recv(BUFSIZE).decode("utf8")
    if msg:
        print(msg)

def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()

set_interval(receive_message, 0.1)

def main():
    while True:
        msg=input(">> ")
        try:
            client_socket.send(bytes(msg,"utf8"))
        except:
            print(sys.exc_info()[1])
if __name__ == "__main__":
    main()