n=int(input())
for i in range(0,n):
    a=int(input())
    k=a*(a+1)//2
    l=list(map(int,input().split()))
    sums=0
    for i in l:
        sums=sums+i
    j=k-sums
    print(j)
        