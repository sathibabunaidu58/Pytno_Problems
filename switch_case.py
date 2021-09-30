'''in python we don not have  switch but we have if, elif,else conditions

examle below see the program
'''
'''
a,b,c=list(map(int,input('enter numbers by , seperated : ').split(',')))
if a>b and a>c:
    print(str(a),'is greater among three numbers')
elif b>c:
    print(str(b),'is greater among three numbers')
else:
    print(str(c),'is greater among three numbers')'''

def odd_even(a):
    if a%2==0:
        print(str(a),'is even number')
    else:
        print(str(a),'is odd number')
a=int(input('enter number : '))
odd_even(a)