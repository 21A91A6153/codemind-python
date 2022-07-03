a=input()
a=a.split()
b=[]
for i in a:
    i=i[::-1]
    b.append(i)
print(*b)