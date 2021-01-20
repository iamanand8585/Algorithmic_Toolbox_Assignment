n=int(input())

n=n%60 #Since 60 is the pisanoperiod for 10

if(n<=1):
    print(n)
else:
    f0=0
    f1=1
    for i in range(2,n+2):
        f0,f1=f1,(f0+f1)%10
    print((f0*f1)%10)
