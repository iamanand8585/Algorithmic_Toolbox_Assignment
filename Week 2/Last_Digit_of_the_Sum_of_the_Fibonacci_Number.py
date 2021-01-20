n=int(input())
def pisanoperiod():
    previous=0
    current=1
    for i in range(10*10):
        previous,current=current,(previous+current)%10
        if(previous==0 and current==1):
            return i+1

n=n%pisanoperiod()

if(n<=1):
    print(n)
else:
    f0=0
    f1=1
    s=0
    for i in range(2,n+1):
        f0,f1=f1,(f0+f1)%10
        s+=f1
    print((s+1)%10)
