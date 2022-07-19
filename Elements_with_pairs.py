n=int(input())
l=list(map(int,input().split()))
k=len(l)
if k%2==0:
    print(*l)
else:
    l.append(0)
    print(*l)