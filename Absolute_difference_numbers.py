n,x=map(int,input().split())
temp=0
sums=0
revsum=0
sumsrev=0
rev=0
ver=0
temp=n
while(n!=0):
    d=n%10
    n=n//10
    sums=sums*10+d#64512
#print(sums)
    
for i in range(0,x):
    e=sums%10
    sums=sums//10
    revsum=revsum*10+e#21
#print(revsum)
while (sums):
    f=sums%10
    sums=sums//10
    sumsrev=sumsrev*10+f
#print(sumsrev)
for i in range(0,x):
    g=sumsrev%10
    sumsrev=sumsrev//10
    rev=rev*10+g
while(rev!=0):
    a=rev%10
    rev=rev//10
    ver=ver*10+a
if ver>revsum:
    w=ver-revsum
    print(w)
else:
    t=revsum-ver
    print(t)
    