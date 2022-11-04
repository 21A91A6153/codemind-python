n=input()
c=[]
for i in n:
    if i in '1234567890':
        c.append(i)
c=set(c)
c=list(c)
c=sorted(c)
c=c[::-1]
d=0
for i in c:
    if int(i)%2==0:
        d+=1
if d==0:
    print(-1)
else:
    for i in range(len(c)-1,-1,-1):
        if int(c[i])%2==0:
           k=c[i]
           c.remove(c[i])
           break
    c.append(k)
    c="".join(c)
    print(c)
    

