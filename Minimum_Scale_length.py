n=int(input())
arr=list(map(int,input().split()))
res=0
mins=9999
for i in arr:
        if(mins>i):
           mins=i
for i in range(mins,0,-1):
        res=0
        for j in arr:
            if(j%i!=0):
                res=1
                break
        if(res==0):
            print(i)
            break