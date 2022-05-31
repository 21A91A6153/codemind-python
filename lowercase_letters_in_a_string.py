n=input()
c=0
for i in n:
    if ord(i)>=95 and ord(i)<=122:
        c=c+1
print(c)