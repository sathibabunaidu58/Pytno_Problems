try:
    with open('readme.txt') as f:
        s = f.read()
        print ('read', len(s), 'bytes.')
except IOError as x:
    if x.errno == errno.ENOENT:
        print('readme.txt', '- does not exist')
    elif x.errno == errno.EACCES:
        print ('readme.txt', '- cannot be read')
    else:
        print('readme.txt', '- some other error')