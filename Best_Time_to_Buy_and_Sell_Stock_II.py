x=int(input())
l=list(map(int,input().split()))
r=reversed(l)
n=0
z=[]
k=sorted(l)
if l==k:
    print(l[-1]-l[0])
    
elif l==r:
    print("0")
else:
    for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
            s=l[i+1]-l[i]
            z.append(s)
    for j in z:
        n=n+j
    print(n)