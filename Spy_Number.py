n=int(input())
sums=0
mul=1
while(n):
    d=n%10
    n=n//10
    sums=sums+d
    mul=mul*d
if mul==sums:
    print("Spy Number")
else:
    print("Not Spy Number")
    