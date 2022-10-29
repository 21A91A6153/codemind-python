n,m=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in range(m):
    c.append(l[i])
b=[]
for i in range(m,len(l)):
    b.append(l[i])
b.extend(c)
print(*b)