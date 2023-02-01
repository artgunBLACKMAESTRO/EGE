def searchnotdel(i:int):
    g=set()
    for z in range(2,int(i**(0.5))+1):
        if i%z==0:
            g.add(z)
            g.add(i//z)
    g=list(g)
    pr=[]
    for z in range(len(g)):
        flag=True
        for k in range(2,int(g[z]**(0.5))+1):
            if g[z]%k==0:
                flag=False
                break
        if flag:
            pr.append(g[z])
    return pr
def searchdel(i:int):
    g = set()
    for z in range(2, int(i ** (0.5)) + 1):
        if i % z == 0:
            g.add(z)
            g.add(i // z)
    return list(g)
b=[]
for i in range(278932, 325397):
    deli=searchnotdel(i)
    for z in range(len(deli)-2):
        for x in range(z+1,len(deli)-1):
            for y in range(x+1,len(deli)):
                if (deli[z]%10==deli[x]%10 and deli[y]%10==deli[x]%10) and ((deli[z]*deli[x]*deli[y]) == i):
                    b.append(i)
print(len(b),max(b))


