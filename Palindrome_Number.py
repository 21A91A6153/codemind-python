n=int(input())
for i in range(0,n+1):
    a=int(input())
    rev=0
    temp=a
    while(a!=0):
        d=a%10
        a=a//10
        rev=rev*10+d
    if rev==temp:
        print("True")
    else:
        print("False")