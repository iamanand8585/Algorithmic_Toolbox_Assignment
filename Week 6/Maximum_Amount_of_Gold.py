

def optimal_weight(W, w):
    value = [[0]*(len(w)+1) for _ in range(W+1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            value[j][i] = value[j][i-1]
            if w[i-1] <= j:
                val = value[j-w[i-1]][i-1] + w[i-1]
                if val >= value[j][i]:
                    value[j][i] = val
    return value[W][len(w)]             



w,n=input().split()
w=int(w)
n=int(n)

l=list(map(int,input().strip().split()))
print(optimal_weight(w,l))