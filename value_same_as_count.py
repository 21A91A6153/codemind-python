n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)==i:
        b.append(i)
c=0
for i in b:
    c=c+1
print(c)