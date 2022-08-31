n=int(input())
c=[]
for i in range(1,n):
    if n%i==0:
        c.append(i)
b=[]
for i in c:
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d+=1
    if d==2:
        b.append(i)
a=[]
for i in b:
    k=n//i
    if k in b and k*i==n and k!=i:
        a.append(i)
if a==[]:
    print(-1)
else:
    print(*a)
    