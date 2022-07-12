n=input()
n=n.lower()
n=set(n)
n=sorted(n)
b=[]
for i in n:
    if i!=" ":
        b.append(i)
b="".join(b)
print(b)