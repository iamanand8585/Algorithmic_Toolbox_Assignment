def maximun_revenue(n,a,b):
    a.sort()
    b.sort()
    s=0
    for i in range(n):
        s+=a[i]*b[i]
    return s


n=int(input())
a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
print(maximun_revenue(n,a,b))