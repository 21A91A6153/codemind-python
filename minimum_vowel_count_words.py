a=input()
b=[]
a=a.split()
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    b.append(c)
t=min(b)
print(b.count(t))
    

        