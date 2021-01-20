n=int(input())

l=[]
s=0

for i in range(n):

    if(s==n):
        break
    s+=i+1
    if(s>n):
        s-=i
        l[len(l)-1]=i+1
    else:
        l.append(i+1)
print(len(l))
print(*l,sep=' ') 
        
