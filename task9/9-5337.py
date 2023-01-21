a=open('9-5337')
d=a.readlines()
a.close()
def test1(g:list):
    return g[-1]<(g[0]+g[1]+g[2])
def test2(g: list):
    return ((g[0]+g[1])==(g[2]+g[3])) or ((g[0]+g[2])==(g[1]+g[3])) or ((g[0]+g[3])==(g[1]+g[2]))
count=0
for i in range(len(d)):
    g=list(map(int,d[i].split('\t')))
    g.sort()
    if test1(g) and test2(g):
        count+=1
print(count)

