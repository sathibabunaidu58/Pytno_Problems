def common(a,b):    
    a=set(a)
    b=set(b)
    print(list(a&b))


a = list(map(int,input('enter values separated by space: ').split()))
b = list(map(int,input('enter values separated by space: ').split()))
common(a,b)