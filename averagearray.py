def add(a):
    if len(a)>=1:
        print(sum(a)/len(a))
    else:
        print('Not Valid')
a=list(map(int,input('enter values separated by space: ').split()))
add(a)
