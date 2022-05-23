import math
n=int(input())
rev=0
if n>0:
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    print(rev)
else:
    k=abs(n)
    while k:
        d=k%10
        k=k//10
        rev=rev*10+d
    print(-rev)
    
    