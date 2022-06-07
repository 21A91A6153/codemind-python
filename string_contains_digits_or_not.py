n=int(input())
for i in range(n):
    a=input()
    c=0
    for i in a:
        if i in '1234567890':
            c=c+1
    if c==0:
        print("No")
    if c>=1:
        print("Yes")
        
            