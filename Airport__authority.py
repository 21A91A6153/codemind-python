n=int(input())
l=[]
c=0
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in a:
        l.append(j)
#print(l)
k=int(input())
#print(k)
for i in l:
    if i<=k:
        c=c+1
    if i>k:
        c=c+2
print(c)
    
    

    