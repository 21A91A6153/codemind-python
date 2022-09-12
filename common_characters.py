n=input()
m=input()
n=n.lower()
m=m.lower()
n=set(n)
m=set(m)
n=n.intersection(m)
c=[]
for i in n:
    if i!=' ':
        c.append(i)
c=sorted(c)
c=''.join(c)
if len(c)==0:
    print(-1)
else:
    print(c)
