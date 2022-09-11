n=input()
n=n.lower()
b=[]
for i in n:
    if i!=" " and n.count(i)==1:
        b.append(i)
b=sorted(b)
k="".join(b)
print(len(k))
