n=input()
b=[]
for i in n:
    if i not in b and i in 'aeiouAEIOU':
        b.append(i)
if b==[]:
    print(-1)
else:
    print(*b)