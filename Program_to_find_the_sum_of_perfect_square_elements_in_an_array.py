import math
n=int(input())
l=list(map(int,input().split()))
sums=0
for i in l:
    for j in range(1,i+1):
        if i==j*j:
            sums+=i
print(sums)
