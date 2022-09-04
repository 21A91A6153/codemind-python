n=int(input())
dec=0
i=0
while n!=0:
    d=n%10
    n=n//10
    dec=dec+d*(8**i)
    i+=1
k=bin(dec)
k=k[2::]
print(k)