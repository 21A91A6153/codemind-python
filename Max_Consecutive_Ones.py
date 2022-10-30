n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n):
    d=0
    for j in range(i,len(l)):
        if l[j]==1:
            d+=1
        else:
            break
    c.append(d)
print(max(c))
