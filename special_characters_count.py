n=input()
c=0
for i in n:
    if ord(i)>=33 and ord(i)<=47:
        c=c+1
    elif ord(i)>=58 and ord(i)<=64:
        c=c+1
    elif ord(i)>=91 and ord(i)<=96:
        c=c+1
    elif ord(i)>=123 and ord(i)<=126:
        c=c+1
print(c)