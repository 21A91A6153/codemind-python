x=int(input())
y=int(input())
sum=0
for i in range(x):
    l=list(map(int,input().split()))
    for i in l:
        sum=sum+i
print(sum)