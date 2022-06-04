n=int(input())
l=list(map(int,input().split()))
c=0
m=0
b=[]
for i in l:
    c=0
    for j in l:
        if i==j:
            c=c+1
    if c==1:
        b.append(i)
        m+=1
if m==0:
    print(-1)
else:
    print(max(b))
        