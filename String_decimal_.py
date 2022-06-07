n=int(input())
for i in range(n):
    a=input()
    k=len(a)
    c=0
    for i in a:
        if i in '1234567890':
            c=c+1
    if c==k:
        print(True)
    else:
        print(False)
        
            