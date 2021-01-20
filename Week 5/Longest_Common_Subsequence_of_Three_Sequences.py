
def lcs3(a, b, c):
    T = [[[0]*(len(a)+1) for _ in range(len(b)+1)] for _ in range(len(c)+1)]
    for i in range(1,len(a)+1):
    	for j in range(1,len(b)+1):
    		for k in range(1,len(c)+1):
    			if a[i-1]==b[j-1]==c[k-1]:
    				T[k][j][i] = T[k-1][j-1][i-1] + 1
    			else :
    				T[k][j][i] = max(T[k-1][j][i],T[k][j-1][i],T[k][j][i-1])


    return T[k][j][i]

n=int(input())
a=list(map(int,input().strip().split()))

m=int(input())
b=list(map(int,input().strip().split()))

o=int(input())
c=list(map(int,input().strip().split()))

print(lcs3(a, b, c))