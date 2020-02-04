from socket import AF_INET,socket,SOCK_STREAM
import _thread, sys
Connection = False
#addresses = {}
clients = set()
BUFSIZE = 1024
host = '0.0.0.0'
port = 8000
ADDR = (host,port)
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)

def receive_message(client_conn,addr):
    client_conn.send(bytes("Enter your name","utf8"))
    name = client_conn.recv(BUFSIZE).decode("utf8")
    msg = "%s has joined the room" %name
    broadcast(msg,client_conn)
    clients.add((client_conn,name))
    while True:
        msg = client_conn.recv(BUFSIZE).decode("utf8")
        if msg:
            final_msg = name + '->' + msg
            broadcast(final_msg,client_conn)

def broadcast(msg,client):
    for data in clients:
        if data[0] == client:
            pass
        else:
            try:
                data[0].send(bytes(msg,"utf8"))
            except:
                print(sys.exc_info()[1])

def main():
    server.listen(3)
    while True:
        try:
            client_conn, client_address = server.accept()
        except:
            print(sys.exc_info()[1])
        print("%s:%s has connected."%client_address)
        _thread.start_new_thread(receive_message,(client_conn,client_address))

if __name__ == "__main__":
    main()