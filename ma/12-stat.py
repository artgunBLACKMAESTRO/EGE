from itertools import product as pr
a=set(pr('12',repeat=20))
b=[i for i in a if i.count('1')==i.count('2')]
m=0
for i in b:
    g='0'+''.join(i)+'0'
    while '00' not in g:
        g=g.replace('012','30')
        if '011' in g:
            g=g.replace('011','20')
            g=g.replace('022','40')
        else:
            g=g.replace('01','10')
            g=g.replace('02','101')
    if g.count('1')==6 and g.count('2')==5:
        m=max(m,g.count('4'))
print(m)
