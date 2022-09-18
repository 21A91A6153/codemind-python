n=input()
n=n.lower()
n=n.split()
c=0
s=n[0]
for i in s:
    for j in n:
        if i in j:
           # print(i)
            continue
        else:
            #print(j)
            break
    else:
        print(i,end='')
        c=c+1
if c==0:
    print(-1)
