a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)>=1:
        b.append(i)
c=0
for i in b:
    if i%2==1:
        c=c+1
print(c)