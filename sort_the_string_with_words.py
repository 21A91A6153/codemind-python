n=input()
n=n.lower()
n=n.split()
c=[]
for i in n:
    if i!=' ' and i not in c:
        c.append(i)
c=sorted(c)
print(*c)
