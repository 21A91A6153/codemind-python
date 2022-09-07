n=int(input())
l=list(map(int,input().split()))
j,k=map(int,input().split())
h=max(l)
for i in l:
    if i<j or i>k:
        if i==h:
            print(i)
c=0
for i in l:
    if i>=j and i<=k:
        if i==h:
            c+=1
if c>=1:
    print(-1)