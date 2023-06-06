with open('26-h') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
mr=0
mm=0
d=[['0']*10000 for _ in range(10000)]
for i in range(len(a)):
    d[a[i][0]][a[i][1]]='1'
for i in range(len(d)):
    j=''.join(d[i])
    if '1'+'0'*11+'1' in j:
        h=i
i=0
print(h)
for i in range(5086,5100):
    print(d[h][i])
while True:
    f=i+12
    if d[h][i]=='1' and d[h][f]=='1':
        print(i)
        break
    i+=1
