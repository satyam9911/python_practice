import socket,threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.bind(('0.0.0.0', 8888))

def receive_message():
    data, ip = my_socket.recvfrom(1024)
    print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))

def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()

set_interval(receive_message, 0.1)

while True:
    message = input("> ")
    message = message.encode()
    my_socket.sendto(message, ("localhost",8888))