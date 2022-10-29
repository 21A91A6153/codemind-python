n=int(input())
l=list(map(int,input().split()))
l.sort()
l=l[::-1]
c=[]
for i in range(len(l)):
    if i%2!=0:
        c.append(l[i])
        c.append(l[i-1])
if n%2!=0:
    c.append(l[n-1])
print(*c)