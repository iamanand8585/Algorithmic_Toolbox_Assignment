
def get_change(m):
    coin=0
    while(m>0):
        if(m>=10):
            coin+=m//10
            m=m-10*(m//10)
        elif(m>=5):
            coin+=m//5
            m=m-5*(m//5)
        elif(m>=1):
            coin+=1
            m=m-1
    return coin

m=int(input())
print(get_change(m))