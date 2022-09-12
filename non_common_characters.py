n=input()
m=input()
n=n.lower()
m=m.lower()
n=set(n)
m=set(m)
l=n
n=n.difference(m)
m=m.difference(l)
c=[]
for i in n:
    if i!=' ':
        c.append(i)
for i in m:
    if i!=' ':
        c.append(i)
c=sorted(c)
c="".join(c)
print(c)

