n=int(input())
sums=0
d=n*n
while d!=0:
    e=d%10
    d=d//10
    sums=sums+e
if sums==n:
    print("Neon Number")
else:
    print("Not Neon Number")