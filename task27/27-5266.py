with open('27-5266A') as f:
    a=f.read()
a=a.split('\n')
ob=int(a[0].split('\t')[1])
a.pop(0)
a=list(map(int,a))
print(ob,a)