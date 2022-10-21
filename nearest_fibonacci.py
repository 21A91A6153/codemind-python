n=int(input())
arr=[]
a=0
b=1
for i in range(1,n+1):
    arr.append(a)
    c=a+b
    a=b
    b=c
for i in range(n):
    if(arr[i]>n):
        break
if(n-arr[i-1] == arr[i]-n):
    print(arr[i-1],arr[i])
elif(n-arr[i-1] > arr[i]-n):
    print(arr[i])
else:
    print(arr[i-1])