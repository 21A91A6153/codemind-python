a=input()
a=a.lower()
b=input()
b=b.lower()
g=[]
h=0
a=a.split()
b=b.split()
for i in a:
    for j in b:
        if i==j:
            g.append(i)
c=[]
for i in g:
    if i not in c and g.count(i)==1:
        c.append(i)
for i in c:
    h=h+1
print(h)