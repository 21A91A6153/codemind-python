n=int(input())
k=0
for i in range(1,n+1):
    c=0
    if n%i==0:
        for j in range(1,int(pow(i*i,0.5))+1):
            if i%j==0:
                c=c+1
        if c!=2:
            k=k+1
print(k)
            
        