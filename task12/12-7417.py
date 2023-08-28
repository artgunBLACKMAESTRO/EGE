def test(c):
    for i in range(2,int(c**(1/2))+1):
        if c%i==0:
            return False
    return True
for n in range(1,1000):
    a='>'+37*'0'+n*'1'+'2'*37
    while '>1' in a or '>2' in a or '>0' in a:
        if '>1' in a:
            a=a.replace('>1','22>',1)
        if '>2' in a:
            a=a.replace('>2','2>',1)
        if '>0' in a:
            a=a.replace('>0','1>',1)
    c=0
    for i in a:
        if i!='>':
            c+=int(i)
    if test(c):
        print(n)
        break