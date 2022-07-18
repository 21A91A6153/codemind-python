n=int(input())
l=list(map(int,input().split()))
c=0
p=0
for i in range(len(l)):
    if(l[i]!=-1):
        c=1
        for j in range(len(l)):
            if(l[i]==l[j] and i!=j):
                c=c+1
                l[j]=-1
        p=p+c//2
print(p)