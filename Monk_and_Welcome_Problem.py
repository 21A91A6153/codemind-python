n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    k=0
    k=a[i]+b[i]
    c.append(k)
print(*c)