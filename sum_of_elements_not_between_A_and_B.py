n=int(input())
l=list(map(int,input().split()))
j,k=map(int,input().split())
c=0
for i in l:
    if i>=j and i<=k:
        c=c+i
#print(c)
k=sum(l)-c
print(k)
        
