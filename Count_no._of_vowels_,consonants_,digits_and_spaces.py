n=input()
n=n.lower()
c=0
k=0
b=0
m=0
for i in n:
    if i in 'aeiou':
        c=c+1
    if i in 'bcdfghjklmnpqrstvwxyz':
        k=k+1
    if i in '1234567890':
        b=b+1
    if i in " ":
        m=m+1
print("Vowels:",c)
print("Consonants:",k)
print("Digits:",b)
print("White spaces:",m)