from itertools import permutations as pr
a=set(pr('ЭФЕКТ',r=5))
b=[]
k=0
for i in a:
    b.append(''.join(i))
for i in range(len(b)):
    glas=[]
    sogl=[]
    for z in range(len(b[i])):
        if b[i][z] in 'ЭЕ':
            glas.append(b[i][z])
        else:
            sogl.append(b[i][z])
    glascopy=glas.copy()
    soglcopy=sogl.copy()
    glascopy.sort()
    soglcopy.sort(reverse=True)
    if (sogl == soglcopy) and (glas == glascopy):
        k+=1
print(k)