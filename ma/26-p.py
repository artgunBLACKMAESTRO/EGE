with open('26-p') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
mr=0
mm=0
d=[['0']*100000 for _ in range(100000)]
for i in range(len(a)):
    d[a[i][0]][a[i][1]]='1'

print(h)
