with open('27-2668B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
k=[0]
D=8
for i in a:
    comb=[x+y for x in i for y in k]
    k={x%D : x for x in sorted(comb,reverse=True)}
    k=k.values()
print(min([x for x in k if x%D!=2]))