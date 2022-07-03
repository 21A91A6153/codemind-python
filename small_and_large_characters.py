a=input()
b=[]
a=a.split()
for i in a:
    k=min(i)
    g=max(i)
    b.append(k)
    b.append(g)
print(*b)
