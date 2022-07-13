a=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)>=1:
        if i%2==0:
            c.append(i)
c=set(c)
h=0
for i in c:
    h=h+1
print(h)