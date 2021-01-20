def fibo_sum(num):
    num=num%60   #Since, 60 is the pisanoperiod for 10
    if(num<=1):
        return num
    else:
        f0=0
        f1=1
        s=0
        for i in range(2,num+1):
            f0,f1=f1,(f0+f1)%10
            s+=f1
        return (s+1)


m,n=input().split()
m=int(m)
n=int(n)

print((fibo_sum(n)-fibo_sum(m-1))%10)