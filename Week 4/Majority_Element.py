def mejority_element(arr,n):
    freq={}

    for i in l:
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1

    for i in freq:
        if(freq[i]>n//2):
            return 1
    return 0

n=int(input())
l=list(map(int,input().strip().split()))

print(mejority_element(l,n))
