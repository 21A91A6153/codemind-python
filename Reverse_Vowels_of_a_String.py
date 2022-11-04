x=input()
c=1
k=[]
s=[]
for i in x:
    if i in 'AEIOUaeiou':
        k.append(i)
for i in x:
    if i in 'AEIOUaeiou':
        s.append(k[-c])
        c+=1
    else:
        s.append(i)
for i in s:
    print(i,end="")