import socket
import select

port = 60003
sockL=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sockL.bind(("",port))
sockL.listen(1)

listOfSockets = [sockL]

print("Listening on port {}".format(port))

while True:
    tup = select.select(listOfSockets,[],[])
    sock = tup[0][0]

    if sock==sockL:
        (sockC,addr)=sockL.accept()
        listOfSockets.append(sockC)
        sockC.send(bytearray("Connected",'ascii'))
        
        for socket in listOfSockets:
            if(socket != sockL and socket != sockC):
                socket.send(bytearray("{}  connected".format(sockC.getpeername()),'ascii'))

    else:
        data = socket.recv(2048)
        if not data:
            listOfSockets.remove(sock)
            sock.close()
            for socket in listOfSockets:
                if(socket != sockL):
                     socket.send(bytearray("{}  disconncted".format(sockC.getpeername()),'ascii'))
        

        else:   
            name="[{}]".format(sock.getpeername())
            for socket in listOfSockets:
                if(socket != sockL):
                    msg= name + data.decode('ascii')
                    socket.send(bytearray(msg,'ascii'))
