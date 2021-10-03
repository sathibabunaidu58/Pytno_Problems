input_list_1 = ['Hello', ' from', 123, 456, ' AskPython']
input_list_2 = [123, 456, ' AskPython']
 
def add_list(ip):
    if isinstance(ip, list):
        result = '' if isinstance(ip[0], str) else 0
        for item in ip:
            if isinstance(item, int) and item > 200:
                raise ValueError('Integer Item has to be <= 200')
            result = result + item
        return result
    else:
        return None
 
try:
    
    res = add_list(input_list_1)
    print(res)
except TypeError as te:
    print(type(te), te)
except ValueError as ve:
    print(type(ve), ve)