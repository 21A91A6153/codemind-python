n=input()
n=n.lower()
n=n.split()
c=0
for i in n:
    for j in range(len(i)//2):
        if i[j] in 'aeiou' and i[-(j+1)] not in 'aeiou':
            c+=1
        if i[j] not in 'aeiou' and i[-(j+1)] in 'aeiou':
            c+=1
print(c)