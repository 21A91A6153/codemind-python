n=int(input())
a=[]
c=[]
while(n):
        d=n%10
        n=n//10
        a.append(d)
for j in range(len(a)-1,-1,-1):
        if(a[j]==6):
            a[j]=9
            break
for j in range(len(a)-1,-1,-1):
        c.append(str(a[j]))
c="".join(c)
print(int(c))