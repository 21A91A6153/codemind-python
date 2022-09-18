n=input()
n=n.lower()
n=n.split()
c=0
s=n[0]
for i in s:
    for j in n:
        if i in j:
            continue
        else:
            break
    else:
        print(i,end='')
        c=c+1
if c==0:
    print(-1)
