n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    l.extend(m)
    l.sort()
    print(*l)