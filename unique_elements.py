a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i not in b and l.count(i)>=1:
        b.append(i)
for i in b:
    print(i,end=" ")