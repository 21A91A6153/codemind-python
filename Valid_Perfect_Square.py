import math
n=int(input())
for i in range(0,n):
    a=int(input())
    k=int(math.sqrt(a))
    if k*k==a:
        print("True")
    else:
        print("False")