n=int(input())
l=list(map(int,input().split()))
k=max(l)
for i in range(1,k*k):
    if i not in l:
        print(i)
        break