a=input()
a=a.lower()
b=input()
b=b.lower()
g=[]
c=0
a=a.split()
b=b.split()
for i in a:
    for j in b:
        if i==j:
            g.append(i)
for i in g:
    c=c+1
print(c)