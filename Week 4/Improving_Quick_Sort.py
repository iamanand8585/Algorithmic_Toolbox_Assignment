import random

def partition3(arr,l,r):
    pivot= arr[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
    	if arr[i] < pivot:
        	arr[i],arr[m1] = arr[m1],arr[i]
        	m1+=1
        	m2+=1
        	arr[i],arr[m2] = arr[m2],arr[i]
    	elif arr[i] == pivot:
        	m2+=1
        	arr[i],arr[m2] = arr[m2],arr[i]
    return m1,m2    	    	






def partition2(arr,l,r):
    pivot= arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def randomized_quick_sort(arr,l,r):
    if(l<r):
        k = random.randint(l, r)
        arr[l], arr[k] = arr[k], arr[l]
        mid1,mid2 = partition3(arr,l,r)
        randomized_quick_sort(arr,l,mid1-1)
        randomized_quick_sort(arr, mid2+1, r)
    return arr
    


n=int(input())
l=list(map(int,input().strip().split()))
lw=0
hg=n-1
for i in randomized_quick_sort(l,lw,hg):
    print(i,end=" ")
