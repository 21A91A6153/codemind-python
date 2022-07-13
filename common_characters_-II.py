n=input()
n=n.lower()
n=set(n)
m=input()
m=m.lower()
m=set(m)
b=[]
for i in n:
    for j in m:
        if i==j:
            b.append(i)
c=0
for i in b:
    if i!=" ":
        c=c+1
print(c)