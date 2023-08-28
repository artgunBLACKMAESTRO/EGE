from itertools import product as pr
a='МЫСЛЬ'
b=[]
for i in a:
    b.append(i)
b.sort()
a=''.join(b)
z=pr(a,repeat=5)
c=0
for i in z:
    c+=1
    j=''.join(i)
    if j[:2]=='ЫЫ':
        k=c
print(k)