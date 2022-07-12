n=input()
n=n.split()
b=[]
for i in range(len(n)-1,-1,-1):
    b.append(n[i])
print(*b)