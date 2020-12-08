import math
import random
import zlib
import collections
with open('exempeltext.txt','r') as file:
    txt = file.read()

byteArr = bytearray(str(txt),"UTF-8")

lentxt = len(txt)
bytelen = len(byteArr)
print(lentxt)
print(bytelen)

# String: 29091     Byte: 30491  UTF-8 has some chars that are bigger thats why the byte value is larger

def makeHisto(byteArr):
    histo = [0]*256
    for i in byteArr:
        histo[i]+=1
    print(histo)
    return histo

def makeProb(histo):
    prob=[0]*256
    n=0
    for i in range(256):
        prob[i]+=histo[i]/len(byteArr)
        print(i,"has a probability",round(prob[i], 4))
        n+=prob[i]
    print(n)
    return prob

def entropi(prob):
    probLenght = len(prob)
    entropiValue = 0
    for i in range(probLenght):
        if prob[i] !=0:
            entropiValue += prob[i]*math.log(1/prob[i], 2)
    print(entropiValue)
    return entropiValue

h=makeHisto(byteArr)
p=makeProb(h)
entropi(p)

#We can compress byteArr to 4.59 byte/char

theCopy = byteArr.copy()
random.shuffle(theCopy)

copyComp = zlib.compress(theCopy)
byteArrComp = zlib.compress(byteArr)

print(len(copyComp))
#19814
print(len(byteArrComp))
#12848



#Entropy 4.59  optimal encoding but no statistical redundancy

#copyComp 5.59 no optimal encoding or statistical redundancy

#byteArrComp 3.88 both optimal encoding and statistical redundancy


t1 = """I hope this lab never ends beacause
        it is so incredibly thrilling!"""
t10 = t1*10

t1ByteArr = bytearray(t1, "UTF-8")
t10ByteArr = bytearray(t10, "UTF-8")
print(len(t1ByteArr))
#74
print(len(t10ByteArr))
#740

t1Comp = zlib.compress(t1ByteArr)
t10Comp = zlib.compress(t10ByteArr)
print(len(t1Comp))
#72
print(len(t10Comp))
#82