def car_fule(m,n,l,d):
    currentfule=0
    no_of_refills=0
    # add 0 at begining and d at end
    l.insert(0,0)
    l.append(d)

    while(currentfule<=n):

        lastfule=currentfule

        while(currentfule<=n and l[currentfule+1]-l[lastfule]<=m):
            currentfule+=1
        if(currentfule==lastfule):
            return -1
        if(currentfule<=n):
            no_of_refills+=1
    return no_of_refills

d=int(input())
m=int(input())
n=int(input())

l=list(map(int,input().strip().split()))
print(car_fule(m,n,l,d))