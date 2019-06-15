import socket
import ParsHtmFileRQ

sock = socket.socket()
sock.connect(('localhost',9090))
sock.send(ParsHtmFileRQ.one('test2.htm')[0].encode())

data = sock.recv(1024).decode()
sock.close()

print(data)