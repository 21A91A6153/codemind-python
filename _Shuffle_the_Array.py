n=int(input())
l=list(map(int,input().split()))
c=[]
b=[]
for i in range(len(l)//2):
    c.append(l[i])
for i in range(len(l)//2,len(l)):
    b.append(l[i])
for i in range(n):
    print(c[i],b[i],end=" ")