a=input()
b=[]
a=a.split()
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    b.append(c)
print(max(b))