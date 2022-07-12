n=input()
n=n.split()
b=[]
for i in n:
    i=i[::-1]
    b.append(i)
for i in range(len(b)-1,-1,-1):
    print(b[i],end=" ")