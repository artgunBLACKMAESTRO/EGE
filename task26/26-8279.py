with open('26-8279') as f:
    a=f.read()
a=a.split('\n')
t,n,m=map(int,a[0].split())
a.pop(0)
a=[list(map(int,a[i].split())) for i in range(len(a))]
a.sort()
print(a)