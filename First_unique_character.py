n=input()
n=n.lower()
b=[]
for i in n:
    if i not in b and n.count(i)==1:
        b.append(i)
if b==[]:
    print(-1)
else:
    print(b[0])