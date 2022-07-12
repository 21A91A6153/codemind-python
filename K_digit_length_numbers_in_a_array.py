n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    i=abs(i)
    if len(str(i))==m:
        c=c+1
print(c)