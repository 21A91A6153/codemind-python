n=input()
n=n.split()
k=n[-1]
m=min(k)
if m.lower() in k:
    print(m.lower())
else:
    print(m)
