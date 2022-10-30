n,m=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in range(n):
    sums=0
    for j in range(i,len(l)):
        sums+=l[j]
        if sums==m:
            d+=1
print(d)