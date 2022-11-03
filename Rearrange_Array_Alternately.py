x=int(input())
for i in range(x):
    k=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    w=[]
    for i in range(len(l)//2):
        w.append(l[(k-1)-i])
        w.append(l[i])
    if(k%2!=0):
        w.append(l[k//2])
    print(*w)