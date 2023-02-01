from itertools import permutations as per
a=set(per('ВОРОН',r=5))
a=list(a)
c=0
for i in a:
    d=''.join(i)
    if 'ОО' not in d:
        c+=1
        print(d)
print(c)