x=int(input())
l=list(map(int,input().split()))
y=int(input())
m=list(map(int,input().split()))
k=[]
s=[]
for i in l:
    k.append(i)
for i in m:
    s.append(i)
k=sorted(k)
s=sorted(s)
if k==s:
    print("True")
else:
    print("False")