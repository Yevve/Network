import socket
def ruleEng(ans1,ans2):
    serverWon=False
    clientWon=False
    
    if ans1==ans2:
        return serverWon,clientWon
    elif ans1=='R':
        if ans2=='S':
            serverWon=True
            return serverWon,clientWon
        else:
            clientWon=True
            return serverWon,clientWon
    elif ans1=='S':
        if ans2=='P':
            serverWon=True
            return serverWon,clientWon
        else:
            clientWon=True
            return serverWon,clientWon
    elif ans1=='P':
        if ans2=='R':
            serverWon=True
            return serverWon,clientWon
        else:
            clientWon=True
            return serverWon,clientWon
    else:
        return("Invalid input")


def serversideGetPlaySocket():
    serverScore=0
    clientScore=0
    gameScore=3
    sockS=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    sockS.bind(('192.168.0.42',60003))
    sockS.listen(1)
    while True:
        print('\nlistening...\n')
        (sockS,addr)=sockS.accept()
        print('connetction from {}'.format(addr))
        while True:
            data=sockS.recv(1024)
            if not data:
                break
            #print('received:',data.decode('ascii'))
            #answer='thanks for the data!'
            #sockS.sendall(bytearray(answer,'ascii'))
            #print('answered',answer)
            
            ansS=input("Enter your choice(R)(P)(S):")
            ansC=data.decode('ascii')

            print('You answered:',ansS)
            print('Client answered:',data.decode('ascii'))
            message="Server answered:{}".format(ansS)
            sockS.sendall(bytearray(message,'ascii'))
            
            
            serverIsWinner,clientIsWinner=ruleEng(ansS,ansC)
            if serverIsWinner:
                serverScore+=1
                result="Server Won! Score {} - {}".format(serverScore,clientScore)
            elif clientIsWinner:
                clientScore+=1
                result ="Client Won! Score {} - {}".format(serverScore,clientScore)
            else:
                result ="Its a Tie!"
  
            print(result)
            sockS.sendall(bytearray(result,'ascii'))

            if clientScore|serverScore is gameScore:
                sockS.close()
                print('client{} disconnected'.format(addr))


def clientsideGetplaySocket(host):
    sock=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    sock.connect(('192.168.0.42',60003))
    
    while True:
        answer=input("Enter your choice(R)(P)(S):")
        sock.sendall(bytearray(answer,'ascii'))
        print('You answered: ',answer)

        data=sock.recv(1024)
        print(data.decode('ascii'))
        data1=sock.recv(1024)
        print('received:',data1.decode('ascii'))

        
    sock.close()



ans= input("Do you wanna be a server (S) or a client (C):")
while ans not in {"C","S"}:
    ans= input("Do you wanna be a server (S) or a client (C):")
if ans=="S":
    sock=serversideGetPlaySocket()
else:
    host=input("Enter the server's name or IP:")
    sock=clientsideGetplaySocket(host)



