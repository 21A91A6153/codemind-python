n=int(input())
l=list(map(int,input().split()))
k=max(l)
for i in range(1,k+1):
    c=0
    for j in l:
        if j%i==0:
            c=c+1
    if c==len(l):
        p=i
print(p)