n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(len(l)):
    if i%2==0:
       # print(i)
        for j in range(l[i]):
            c.append(l[i+1])
print(*c)