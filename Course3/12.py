import socket

mycock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mycock.connect(('localhost',80))
cmd = 'GET http://localhost/AUTO3/index.php HTTP/1.0\n\n'.encode()
mycock.send(cmd)

while True:
    data = mycock.recv(512)
    if len(data) <1:
        break
    print (data.decode())
mycock.close