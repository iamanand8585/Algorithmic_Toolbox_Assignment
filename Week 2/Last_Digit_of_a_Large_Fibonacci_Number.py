n=int(input())
if(n<=1):
    print(n)
else:
    f0=0
    f1=1
    for i in range(2,n+1):
        f0,f1=f1,(f0+f1)%10
    print(f1%10)
