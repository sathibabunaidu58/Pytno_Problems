def copy(a):
    l=[0]*len(a)
    for i in range(len(a)):
        l[i]=a[i]
    print(l)
a=list(map(int,input('enter values separated by space: ').split()))

copy(a)