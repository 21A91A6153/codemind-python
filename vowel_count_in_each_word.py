a=input()
c=0
a=a.split()
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    print(c,end=" ")