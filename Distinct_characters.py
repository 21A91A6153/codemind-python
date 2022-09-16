n=input()
n=n.lower()
c=[]
for i in n:
    if i not in c and n.count(i)==1 and i!=' ':
        c.append(i)
#print(c)
c=sorted(c)
c="".join(c)
print(c)