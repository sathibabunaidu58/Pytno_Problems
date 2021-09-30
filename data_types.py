print(7,'==>it is int type')
print('sathi babu','==>it is string type')
print(2.34,'==>it is float type')
print(True,False,'==>these are boolean type')

# you can test your self

value = input('enter value : ')
if value.isdigit():
    print(type(int(value)))
elif value == 'True' or value == 'False':
    print('Boolean Type')
else :
    print(type(value))