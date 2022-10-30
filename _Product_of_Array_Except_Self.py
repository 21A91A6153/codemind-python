n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    k=1
    for j in range(len(l)):
        if l[i]==l[j]:
            continue
        else:
            k=k*l[j]
    c.append(k)
print(*c)