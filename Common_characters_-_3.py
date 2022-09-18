n=input()
n=n.lower()
n=n.split()
k=[]
s=n[0]
for i in s:
    for j in n:
        if i in j:
            continue
        else:
            break
    else:
        k.append(i)
if k==[]:
    print(-1)
else:
    k=sorted(k)
    print(k[0])

