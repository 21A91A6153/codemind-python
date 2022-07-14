n=int(input())
l=list(map(str,input().split()))
l="".join(l)
dec=0
i=0
l=int(l)
while l!=0:
    d=l%10
    dec=dec+d*pow(2,i)
    i=i+1
    l=l//10
print(dec)