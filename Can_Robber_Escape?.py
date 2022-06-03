n=int(input())
x=list(map(int,input().split()))
odd=0
for i in x:
    if(i%2!=0):
         odd=odd+1
if (odd<=2):
    print("YES")
else:
    print("NO")