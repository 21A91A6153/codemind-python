n=input()
k=input()
if k in n:
    print(True)
    print(n.index(k))
if k not in n:
    print(False)