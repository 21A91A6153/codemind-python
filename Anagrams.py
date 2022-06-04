n=input()
m=input()
n=n.lower()
m=m.lower()
n=''.join(sorted(n))
m=''.join(sorted(m))
if n==m:
    print("True")
else:
    print("False")