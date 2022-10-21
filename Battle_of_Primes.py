def isprime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
    if(c==0):
        return 1
    else:
        return 0
n1=int(input())
n2=int(input())
i=1
while(1):
    tot=n1+n2+i
    if(isprime(tot)):
        print(i)
        break
    i+=1