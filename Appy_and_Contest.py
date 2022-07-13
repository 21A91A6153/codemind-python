n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    k=a//b
    l=a//c
    if k+l>=d:
        print("Win")
    else:
        print("Lose")