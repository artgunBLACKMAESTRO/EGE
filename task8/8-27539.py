from itertools import product
a=set(product('БОРИС',repeat=6))
k=0
for z in a:
    z=''.join(z)
    if z.count('Б')==1 and z.count('Р')==1 and z.count('С')<=1:
        k+=1
print(k)
