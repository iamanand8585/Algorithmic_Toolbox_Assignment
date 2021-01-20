a,b=input().split()
a=int(a)
b=int(b)

def lcm(a,b):
    if(b==0):
        return a
    else:
        return lcm(b,a%b)
l=int((a*b)/lcm(a,b))
print(l)