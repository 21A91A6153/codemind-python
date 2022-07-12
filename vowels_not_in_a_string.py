n=input()
b=[]
for i in n:
    if i in 'aeiou':
        b.append(i)
c=['a','e','i','o','u']
for i in b:
    if i in c:
        c.remove(i)
if c==[]:
    print(0)
else:
    print(*c)
        