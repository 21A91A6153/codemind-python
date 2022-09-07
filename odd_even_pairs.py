n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
e=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
if len(a)<len(b):
    for i in range(len(a)):
        e.append(b[i])
        e.append(a[i])
    for i in range(len(a),len(b)):
        e.append(b[i])
    if n%2==0:
        print(*e)
    else:
       e.append(0)
       print(*e)
if len(b)<len(a):
    for i in range(len(b)):
        e.append(b[i])
        e.append(a[i])
    for i in range(len(b),len(a)):
        e.append(a[i])
    if n%2==0:
        print(*e)
    else:
        e.append(0)
        print(*e)
else:
    for i in range(len(b)):
        e.append(b[i])
        e.append(a[i])
    print(*e)
        
    
        