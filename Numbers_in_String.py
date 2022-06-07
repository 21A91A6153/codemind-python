n=input()
sums=0
for i in n:
    if i in "1234567890":
        sums=sums+int(i)
print(sums)