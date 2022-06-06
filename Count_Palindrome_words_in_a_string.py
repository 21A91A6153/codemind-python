n=input()
n=n.lower()
k=n.split()
c=0
for i in k:
    temp=i
    l=i[::-1]
    if temp==l:
        c=c+1
print(c)