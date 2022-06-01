n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in l:
    if i%2==0:
        c=c+1
    else:
        s=s+1
print(c,s)