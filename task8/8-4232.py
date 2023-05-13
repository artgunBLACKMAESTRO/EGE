from itertools import permutations as pr

a=set(pr('ЛОГАРИФМ',r=5))
c=0
for i in a:
    j=''.join(i)
    j=j.replace('Г','Л')
    j = j.replace('Р', 'Л')
    j = j.replace('Ф', 'Л')
    j = j.replace('М', 'Л')
    j = j.replace('А', 'О')
    j = j.replace('И', 'О')
    if 'ЛЛ' not in j and 'ОО' not in j:
        c+=1
print(c)
