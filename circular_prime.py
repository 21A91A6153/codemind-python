n=int(input())
rev=0
c=0
k=0
temp=n
for i in range(1,int(pow(n*n,0.5))+1):
    if n%i==0:
        c=c+1
while(n!=0):
    d=n%10
    n=n//10
    rev=rev*10+d
for j in range(1,int(pow(rev*rev,0.5))+1):
    if rev%j==0:
        k=k+1
if c==2 and k==2:
    print("circular prime")
elif c==2 and k!=2:
    print("prime but not a circular prime")
else:
    print("not prime")
    