def add(a,c):
    if c in a:
        a.remove(c)
        print(a)
    else:
        print('the value not present in given array')
a=list(map(int,input('enter values separated by space: ').split()))
c=int(input('enter value you want find: '))
add(a,c)
