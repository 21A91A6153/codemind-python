n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(3,len(l)):
    if l[i]==l[i-1]+l[i-2]:
        c+=1
if c+3==n:
    print("yes")
else:
    print("no")