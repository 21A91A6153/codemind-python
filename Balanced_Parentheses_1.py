n=input()
a=0
b=0
c=0
d=0
g=0
h=0
for i in n:
    if i=='(':
        a=a+1
    elif i==')':
        b=b+1
    elif i=='{':
        c=c+1
    elif i=='}':
        d=d+1
    elif i=='[':
        g=g+1
    elif i==']':
        h=h+1
if a==b and c==d and g==h:
    print('True')
else:
    print('False')
    