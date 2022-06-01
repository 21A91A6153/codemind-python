n=int(input())
l=list(map(int,input().split()))
k=max(l)
c=0
s=0
m=0
while k:
    d=k%10
    k=k//10
    c+=1
for i in l:
    s=0
    while i:
        d=i%10
        i=i//10
        s+=1
    if c==s:
        m=m+1
print(m)
        