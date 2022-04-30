n=int(input())
sum=0
temp=0
temp=n
while n!=0:
    d=n%10
    n=n//10
    sum=sum+d
if temp%sum==0:
    print("True")
else:
    print("False")