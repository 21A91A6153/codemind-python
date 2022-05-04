a,b=map(int,input().split())
gcd=0
lcm=0
for i in range(1,a+1 and b+1,1):
    if a%i==0 and b%i==0:
        gcd=i
lcm=(a*b)//gcd
print(lcm)