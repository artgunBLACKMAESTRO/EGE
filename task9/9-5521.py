with open('9-5521') as f:
    a=f.readlines()
j=0
for i in range(len(a)):
    g=list(map(int,a[i].split('\t')))
    s=set(g)
    s=list(s)
    g.sort()
    c=0
    for z in range(len(g)-1):
        if g[z]==g[z+1]:
            c=z
            b=g[z]
    g.pop(c)
    g.pop(c)
    for z in range(len(g)):
        z+=g[z]
    z=z/4
    if len(s)==5 and( z<=(2*b)):
        j+=1
print(j)
