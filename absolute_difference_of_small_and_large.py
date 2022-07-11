a=input()
a=a.split()
b=[]
for i in a:
    t=abs(ord(min(i))-ord(max(i)))
    b.append(t)
print(*b)