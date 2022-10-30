n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
c=[]
for i in range(len(k)):
        c.insert(k[i],l[i])
print(*c)