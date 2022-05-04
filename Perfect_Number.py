n=int(input())
sums=0
for i in range(1,n):
    if n%i==0:
        sums=sums+i
if sums==n:
    print("True")
else:
    print("False")