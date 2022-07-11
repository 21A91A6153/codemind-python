a=input()
a=a.lower()
a=a.split()
c=0
for i in a:
    temp=i
    k=i[::-1]
    l="".join(k)
    if temp==l:
        c=c+1
print(c)
    