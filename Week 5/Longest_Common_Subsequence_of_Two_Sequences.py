def lcs2(a, b):
	T = [[0]*(len(a)+1) for _ in range(len(b)+1)]
	for i in range(1,len(a)+1):
		for j in range(1,len(b)+1):
			if a[i-1] == b[j-1]:
				T[j][i] = 1+ T[j-1][i-1]
			else:
				T[j][i] = max(T[j][i-1],T[j-1][i])
	return T[j][i]


n=int(input())
a=list(map(int,input().strip().split()))

m=int(input())
b=list(map(int,input().strip().split()))
print(lcs2(a, b))