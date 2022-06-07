n=int(input())
for i in range (0,n):
    a=input()
    temp=a
    k=a[::-1]
    l="".join(k)
    if temp!=l:
        print("NO")
    else:
        h=len(l)
        if h%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")