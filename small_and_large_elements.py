n=input()
n=n.split()
for i in n:
    k=min(i)
    break
for i in range(len(n)-1,-1,-1):
    m=max(n[i])
    break
print(k,m)