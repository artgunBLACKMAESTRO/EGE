for n in range(1,1002):
    a=bin(n)[2:]
    if n%11==0:
        c=0
        for i in a:
            if i=='0':
                c+=1
        a=a+c*'0'
    else:
        c = 0
        for i in a:
            if i == '1':
                c += 1
        a =c * '1'+a
    if int(a,2)%227==0:
        print(n)
        break