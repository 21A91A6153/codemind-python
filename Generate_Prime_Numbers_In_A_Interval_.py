n=int(input())
m=int(input())
c=0
for i in range(n,m):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print(i)
