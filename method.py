def method(a,b):
    print('incremented value')
    result=0
    for i in range(a):
        result+=i
        print(result)
    sum=b
    print('decremented values')
    for j in range(b):
        sum-=1
        print(sum)
a=int(input('entern value for increment: '))
b=int(input('enter value for decrement: '))
method(a,b)