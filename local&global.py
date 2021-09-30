# for global varible 
''' we defined the a value in otside of the function
we can use this a value inside of the function too'''

a='global'
def fun():
    
    print('this is : ',a)
fun()
print('this is : ',a)

''' but in this we can not use a in outside of 
the function because this scope is only in the
 function range only'''


def fun():
    a='local'
    print('this is : ',a)
fun()
print('this is : ',a)