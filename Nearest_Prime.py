t=int(input())
for k in range(t):
    n=int(input())
    k=0
    b=0
    for i in range(n+1,n*n):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            k=i
            break
    for i in range(n,0,-1):
        c=0
        b=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            b=i
            break
    if abs(n-b)<abs(k-n):
        print(b)
    elif abs(k-n)<abs(n-b):
        print(k)
    else:
        print(b)
        