a=input()
b=[]
a=a.split()
c=[]
for i in a:
    k=min(i)
    g=max(i)
    b.append(k)
    c.append(g)
sums=0
edd=0
for i in b:
    sums=sums+ord(i)
for i in c:
    edd=edd+ord(i)
print(abs(sums-edd))