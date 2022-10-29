n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    m=l.pop()
    l.insert(0,m)
print(*l)