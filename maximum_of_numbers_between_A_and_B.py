a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
k=0
j=0
for i in l:
    if i>=b and i<=c:
        k+=1
        if j<i:
            j=i
if k==0:
    print(-1)
else:
    print(j)


