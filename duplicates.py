def duplicates(a):
    c=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                c.append(a[i])
    print(c)


a = list(map(int,input('enter values separated by space: ').split()))
duplicates(a)