a,b,c=list(map(int,input('enter numbers by , seperated : ').split(',')))
if a>b and a>c:
    print(str(a),'is greater among three numbers')
elif b>c:
    print(str(b),'is greater among three numbers')
else:
    print(str(c),'is greater among three numbers')