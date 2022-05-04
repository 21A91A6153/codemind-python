n=int(input())
while(n!=0):
    d=n%10
    n=n//10
    if d%2==1 and n%2==1:
        print("Odd")
        break
    elif d%2==0 and n%2==0:
        print("Even")
        break
    else:
        print("Mixed")
        break