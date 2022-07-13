def prime(i):
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    else:
        return 1
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if i==1:
        continue
    if prime(i):
        c=c+1
print(c)
        