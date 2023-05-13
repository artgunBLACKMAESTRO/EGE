from itertools import product as pr
a=set(pr('0123456',repeat=5))
k=0
for i in a:
    j=''.join(i)
    c1=0
    c2=0
    for z in j:
        if int(z)%2==0:
            c2+=int(z)
        else:
            c1+=int(z)
    if j.count('6')==1 and c2<c1 and j[0]!='0':
        k+=1
print(k)