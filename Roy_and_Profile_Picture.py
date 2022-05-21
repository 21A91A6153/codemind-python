n=int(input())
m=int(input())
for i in range(0,m):
    a,b=map(int,input().split())
    if(a>=n and b>=n):
        if a==b:
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")
    