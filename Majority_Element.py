n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c=0
    for j in l:
        if i==j:
            c=c+1
    if c>n//2:
        print(i)
        break
        