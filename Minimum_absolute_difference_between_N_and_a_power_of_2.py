n=int(input())
for i in range(n):
    if(n<=pow(2,i)):
        a=i-1
        b=i;
        break;
c=n-pow(2,a);
d=pow(2,b)-n;
if(c<d):
    print(c)
else:print(d)