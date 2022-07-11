a=input()
b=input()
a=a.lower()
b=b.lower()
a=set(a)
b=set(b)
if a==b:
    print(True)
else:
    print(False)