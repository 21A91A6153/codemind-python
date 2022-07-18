n=int(input())
b=[]
for i in range(n+1,n*n):
    temp=i
    rev=0
    while i:
        d=i%10
        i=i//10
        rev=rev*10+d
    if temp==rev:
        b.append(rev)
for i in b:
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if c==0:
        print(i)
        break
        