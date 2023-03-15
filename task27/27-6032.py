with open('27_6032B.txt') as f:
    a=f.read().strip()
a=a.split('\n')
a.pop(0)
for i in range(len(a)):
    a[i]=list(map(int,a[i].split(' ')))
    a[i].sort()
maxresult=0
raz=[]
D=13
for i in range(len(a)):
    maxresult+=max(a[i])
    if (max(a[i])-min(a[i]))%13!=0:
        raz.append(max(a[i])-min(a[i]))
if maxresult%13==0:
    print(maxresult-min(raz))
else:
    print(maxresult)