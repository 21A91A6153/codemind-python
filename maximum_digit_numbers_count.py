n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    b.append(abs(i))
k=max(b)
c=0
while k!=0:
    d=k%10
    k=k//10
    c+=1
r=0
for i in l:
    a=0
    temp=i
    i=abs(i)
    while i:
        d=i%10
        i=i//10
        a+=1
    if a==c:
        print(temp,end=" ")