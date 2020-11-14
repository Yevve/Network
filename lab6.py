import socket


sockS=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sockS.bind(('0.0.0.0',80))
sockS.listen(1)
while True:
    (sockC,addr)=sockS.accept()
    data=sockC.recv(1024).decode('ascii')
    if not data:
        break
    print(data)
    sockC.sendall(bytearray(data,'ascii'))
    sockC.close