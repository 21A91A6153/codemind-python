a=input()
a=a.lower()
b=input()
b=b.lower()
g=[]
c=0
a=a.split()
b=b.split()
for j in b:
    for i in a:
        if j==i:
            g.append(j)
print(*g)