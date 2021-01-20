
n=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(l[-2]*l[-1])

"""# Without Using Sort
#Failed Some Cases
n=int(input())
l=[int(i) for i in input().split()]

maxindex1=-1

for i in range(n):
    if(maxindex1==-1 or l[i]>l[maxindex1]):
        maxindex1=i 

maxindex2=-1

for i in range(n):
    if(l[i]!=l[maxindex1] and (maxindex2==-1 or l[i]>l[maxindex2])):
        maxindex2=i

print(l[maxindex2]*l[maxindex1])"""

