def odd_even(a):
    for i in a:
        if i%2==0:
            print(str(i),'is even number')
        else:
            print(str(i),'is odd number')
a = list(map(int,input('enter values separated by space: ').split()))
odd_even(a)

