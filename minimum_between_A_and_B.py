a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
k=0
j=l[b]
for i in l:
    if i>=b and i<=c:
        k+=1
        if i<j:
            j=i
if k==0:
    print(-1)
else:
    print(j)


