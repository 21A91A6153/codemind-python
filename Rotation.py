n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    d=0
    for i in range(b):
        k=l.pop()
        l.insert(0,k)
    print(*l)