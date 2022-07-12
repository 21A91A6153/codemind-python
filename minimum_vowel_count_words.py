a=input()
b=[]
a=a.split()
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    b.append(c)
t=max(b)
k=0
for i in b:
    if t==i:
        k=k+1
print(k)