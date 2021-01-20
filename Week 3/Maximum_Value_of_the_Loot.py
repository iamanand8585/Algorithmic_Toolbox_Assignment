def get_optimal_value(capacity, weights, values):
    value = 0
    l=[]
    for i in range(len(weights)):
        l.append(values[i]/weights[i])

    while True:
        if(capacity==0):
            break
        a=min(weights[l.index(max(l))],capacity)
        value+=a*max(l)
        capacity-=a
        weights[l.index(max(l))]-=a
        l[l.index(max(l))]=0
        if(sum(l)==0):
            break
    return value


if __name__ == "__main__":
    n,capacity=input().split()
    n=int(n)
    capacity=int(capacity)

    values = []
    weights = []
    for i in range(n):
        v,w=input().split()
        values.append(int(v))
        weights.append(int(w))
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

