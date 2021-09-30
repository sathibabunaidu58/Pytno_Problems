def add(a,c):
    if c in a:
        for i,j in enumerate(a):
            if j==c:
                print(i)
    else:
        print('the value not present in given array')
a=list(map(int,input('enter values separated by space: ').split()))
c=int(input('enter value you want find: '))
add(a,c)
