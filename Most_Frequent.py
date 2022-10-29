n=int(input())
l=list(map(int,input().split()))
k=set(l)
k=list(k)
c=[]
for i in k:
    c.append(l.count(i))
g=max(c)
g=c.index(g)
print(k[g])