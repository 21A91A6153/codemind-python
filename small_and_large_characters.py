a=input()
a=a.split()
b=[]
for i in a:
    k=min(i)
    h=max(i)
    b.append(k)
    b.append(h)
print(*b)