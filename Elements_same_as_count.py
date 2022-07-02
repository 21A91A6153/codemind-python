a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)==i:
        b.append(i)
if b==[]:
    print("-1")
else:
    print(*b)
        