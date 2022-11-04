x=input()
z=[]
c=1
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        c+=1
    else:
        z.append(c)
        c=1
z.append(c)
print(max(z))