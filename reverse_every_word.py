n=input()
n=n.split()
b=[]
for i in n:
    i=i[::-1]
    b.append(i)
print(*b)