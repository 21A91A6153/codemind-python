n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
j=[]
for i in l:
    for u in k:
        if i==u and i not in j:
            j.append(i)
print(*j)