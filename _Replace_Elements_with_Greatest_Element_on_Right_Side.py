n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n):
    m=0
    for j in range(i+1,len(l)):
        if m<l[j]:
            m=l[j]
    c.append(m)
c.pop()
c.append(-1)
print(*c)
    