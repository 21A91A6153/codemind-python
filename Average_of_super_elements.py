a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)==i:
        b.append(i)
c=0
s=0
avg=0
if b==[]:
    print("-1")
else:
    for i in b:
        c=c+1
        s=s+i
    avg=s/c
    print("%.2f"%avg)