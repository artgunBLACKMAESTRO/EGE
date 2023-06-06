from itertools import permutations as product
a=product('АДЕЛНОР',r=7)
c=0
for i in a:
    j=''.join(i)
    c+=1
    if c==2:
        print(j)
    if c==4321:
        print(j)