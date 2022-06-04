n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    j=i*i
    k.append(j)
j=sorted(k)
print(*j)