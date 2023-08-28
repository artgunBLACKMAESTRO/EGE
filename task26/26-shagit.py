with open('26-shagit') as f:
    a=f.read().strip()
a=a.split('\n')
a.pop(0)
k=int(a.pop(0))
a=[list(map(int,i.split())) for i in a]
d=[[0 for i in range(841)] for _ in range(k+1)]
l=0
for i in range(len(a)):
    if a[i][0]<=810:
        flag=True
        for z in range(a[i][0],a[i][0]+31):
            if d[a[i][1]][z]==1:
                flag=False
                break
        if flag:
            for z in range(a[i][0], a[i][0] + 31):
                d[a[i][1]][z] = 1
            l+=1
            c=a[i][1]
        else:
            for z in range(1,len(d)):
                if z!=a[i][1]:
                    if d[z][a[i][0]:a[i][0]+31].count(1)==0:
                        l+=1
                        c=z
                        for w in range(a[i][0], a[i][0] + 31):
                            d[z][w] = 1

print(l,c)