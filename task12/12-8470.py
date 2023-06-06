for n in range(6,10000):
    a='1'+n*'5'+'2'+n*'5'
    while '15' in a or '255' in a or '555' in a:
        if '15' in a:
            a=a.replace('15','2',1)
        if '255' in a:
            a=a.replace('255','1',1)
        if '555' in a:
            a=a.replace('555','12')
    c=0
    for i in a:
        c+=int(i)
    if len(str(c))==3:
        b=n
print(b)
