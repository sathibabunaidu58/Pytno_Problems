def ins(a,c):
    if c[0]<len(a):
        a.insert(c[0],c[1])
        print(a)
    else:
        print('please enter the index in renge',len(a))
    
a=list(map(int,input('enter values separated by space: ').split()))
c=list(map(int,input('enter index and value separated by space: ').split()))
ins(a,c)