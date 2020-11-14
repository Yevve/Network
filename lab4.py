
def fibonacci(maxAmount):
    a,b=0,1
    while a<maxAmount:
        yield a
        a,b=b,a+b
for i in fibonacci(1000000):
    print (i)
