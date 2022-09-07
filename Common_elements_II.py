a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c=l
d=m
k=[]
l=set(l)
m=set(m)
j=l
l=l.difference(m)
m=m.difference(j)
l=list(l)
m=list(m)
#print(l,m)
for i in c:
    for u in l:
        if u==i:
           k.append(i)
for i in d:
    for u in m:
        if u==i:
          k.append(i)
print(*k)