n=int(input())
l=list(map(int,input().split()))
k=sum(l)
if k%4==0:
    print("X")
else:
    print("Y")