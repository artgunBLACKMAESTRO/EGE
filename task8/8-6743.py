from itertools import product
a=product('АЙКОС',repeat=5)
k=0
for i in a:
    k+=1
    g=''.join(i)
    if g.count('О')<=1 and 'СС' not in g:
        print(k)