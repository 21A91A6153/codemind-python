n=input()
n=n.split()
b=[]
for i in range(len(n)):
    if i%2==0:
        n[i]=n[i][::-1]
    b.append(n[i])
print(*b)