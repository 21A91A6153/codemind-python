a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    while i!=0:
        d=i%10
        if d==0:
            break
        if temp%d!=0:
            break
        i=i//10
        if i==0:
            print(temp,end=" ")