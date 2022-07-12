n=input()
n=set(n)
c=0
for i in n:
    if i in 'aeiou':
        c=c+1
if c>=5:
    print(True)
else:
    print(False)
        