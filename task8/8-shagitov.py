from itertools import product as pr
a=pr('АКМСУ',repeat=5)
c=0
for i in a:
    c+=1
    j=''.join(i)
    if j=='КУМАС':
        print(c)