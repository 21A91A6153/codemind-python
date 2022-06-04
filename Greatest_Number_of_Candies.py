n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=max(l)
c=[]
for i in l:
    if m+i>=k:
        c.append("True")
    else:
        c.append("False")
print(*c)
        