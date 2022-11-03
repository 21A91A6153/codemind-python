x=int(input())
k=[]
z=[]
a=0
b=0
for i in range(0,x):
    l=list(map(int,input().split()))
    s=l[::-1]
    k.append(l[i])
    z.append(s[i])
for i in k:
    a=a+i
a=str(a)
for i in z:
    b=b+i
b=str(b)
print("Principal Diagonal:"+a)
print("Secondary Diagonal:"+b)
