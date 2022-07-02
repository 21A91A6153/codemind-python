a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)==i:
        b.append(i)
avg=0
s=0
c=0
if b==[]:
    print("-1")
else:
    for i in b:
        s=s+i
        c=c+1
    avg=s/c
    print("%.2f"%avg)
        
    