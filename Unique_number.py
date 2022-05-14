n=int(input())
a=0
b=0
c=0
d=0
f=0
e=0
g=0
h=0
i=0
while(n!=0):
    w=n%10
    n=n//10
    if w==1:
        a=a+1
    elif w==2:
        b=b+1
    elif w==3:
        c=c+1
    elif w==4:
        d=d+1
    elif w==5:
        e=e+1
    elif w==6:
        f=f+1
    elif w==7:
        g=g+1
    elif w==8:
        h=h+1
    elif w==9:
        i=i+1
if (a>1 or b>1 or c>1 or d>1 or e>1 or f>1 or g>1 or h>1 or i>1):
    print("Not Unique Number")
else:
    print("Unique Number")