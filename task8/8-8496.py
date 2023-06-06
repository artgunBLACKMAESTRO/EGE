from itertools import product
a=product('АВОРТ',repeat=6)
c=0
for i in a:
    j=''.join(i)
    c+=1
    if j=='ВОРОТА':
        print(c)
