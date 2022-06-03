a=int(input())
l=list(map(int,input().split()))
sums=0
es=0
for i in range(len(l)):
    if i%2==0:
        sums=sums+l[i]
    else:
        es=es+l[i]
k=sums-es
if k==0:
    print("YES")
else:
    print("NO")
        
        