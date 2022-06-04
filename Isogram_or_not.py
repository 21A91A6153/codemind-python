n=input()
k=len(n)
n=set(n)
c=0
for i in n:
        c=c+1
if c==k:
    print("True")
else:
    print("False")