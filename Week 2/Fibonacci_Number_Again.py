n,m=input().split()
n=int(n)
m=int(m)

def pisanoperiod(m):
    previous=0
    current=1
    for i in range(m*m):
        previous,current=current,(previous+current)%m
        if(previous==0 and current==1):
            return i+1

n=n%pisanoperiod(m)

if(n<=1):
    print(n)
else:
    f0=0
    f1=1
    for i in range(2,n+1):
        f0,f1=f1,(f0+f1)%m
    print(f1%m)

