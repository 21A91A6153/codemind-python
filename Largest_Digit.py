n=int(input())
k=0
while n!=0:
    d=n%10
    n=n//10
    if(k<d):
        k=d
print(k)