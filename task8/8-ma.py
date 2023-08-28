from itertools import product as pr
a=pr('АВОПР',repeat=4)
c=0
for i in a:
    j=''.join(i)
    c+=1
    if j[0]=='П':
        print(c)
        break