x=int(input())
for i in range(x):
    k=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j:
                if(l[i]+l[j] in l):
                    c+=1
                else:
                    pass
    if(c==0):
        print("-1")
    else:
        print(c//2)
    c=0