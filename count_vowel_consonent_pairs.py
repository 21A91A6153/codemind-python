n=input()
c=0
k=n[::-1]
for i in range(len(n)//2):
    if n[i] in 'aeiouAEIOU' and k[i] not in 'aeiouAEIOU':
        if n[i]!=' ' and k[i]!=' ':
            c+=1
    elif n[i] not in 'aeiouAEIOU' and k[i] in 'aeiouAEIOU':
        if n[i]!=' ' and k[i]!=' ':
            c+=1
print(c)