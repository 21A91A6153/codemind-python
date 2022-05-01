n=int(input())
c=0
temp=0
temp=n
sum=0
while temp!=0:
    d=temp%10
    temp=temp//10
    c+=1
#print(c)
temp=n
while temp!=0:
    d=temp%10
    temp=temp//10
    sum=sum+d**c
    c=c-1
if sum==n:
    print("True")
else:
    print("False")