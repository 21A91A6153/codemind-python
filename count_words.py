n=input()
n=n.split()
c=0
b='AEIOUaeiou'
d="bcdfghjklmnpqrstvwxyz"
for i in n:
    if i[0] in b and i[-1] in d:
        c=c+1
print(c)