def remove_duplicates(a):
    a=set(a)
    print(list(a))


a = list(map(int,input('enter values separated by space: ').split()))
remove_duplicates(a)