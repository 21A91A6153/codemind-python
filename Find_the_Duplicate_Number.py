n=int(input())
b=[]
a=list(map(int,input().split()))
for i in a:
    if i not in b and a.count(i)>1:
        b.append(i)
for i in b:#*b
    print(i)


            