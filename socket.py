#import socket
import _socket as socket

socket.setdefaulttimeout(2)
s = socket.socket()

s.connect(("192.168.95.149",21))
ans = s.recv(1024)
print ans