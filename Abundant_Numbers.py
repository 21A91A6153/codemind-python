n=int(input())
temp=0
for i in range(1,n):
    if n%i==0:
     temp=temp+i
if temp>n:
    print("True")
else:
    print("False")