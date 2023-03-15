with open('27-2681B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
D=10
k=[0]
for i in a:
    comb={x+y for x in i for y in k}
    k={x%D : x for x in sorted(comb)}.values()
print(k.mapping.get(8))