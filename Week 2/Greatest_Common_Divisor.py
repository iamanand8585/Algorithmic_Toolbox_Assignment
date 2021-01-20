a,b=input().split()
a=int(a)
b=int(b)
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(a,b))