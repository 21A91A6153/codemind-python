a=int(input())
l=list(map(int,input().split()))
b=[]
m=0
for i in l:
    c=0
    for j in l:
        if i==j:
           # print(i,j)
            c=c+1
    if c==1:
        b.append(i)
        m=m+1
if m==0:
    print(-1)
else:
    print(*b)