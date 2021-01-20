
def binary_search_it(arr,low,high,key):
    while(low<=high):
        mid=low+(high-low)//2
        if(key==arr[mid]):
            return mid
        elif(k<arr[mid]):
            high=mid-1
        else:
            low=mid+1
    return -1


l1=list(map(int,input().strip().split()))
n=l1[0]
arr1=l1[1:]

l2=list(map(int,input().strip().split()))
k=l2[0]
arr2=l2[1:]

for k in arr2:
    lw=0
    hg=len(arr1)-1
    print(binary_search_it(arr1,lw,hg,k),end=" ")

