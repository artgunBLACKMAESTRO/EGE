with open('24-241') as f:
    a=f.read()
m=0
c=0
a=a.split('F')
a.pop(0)
a.pop(-1)
print(a)
for i in range(len(a)):
    if len(a[i])>0:
        if a[i].count('E')>=5:
            g=a[i].split('E')
            flag=True
            for z in range(1,len(g)-1):
                if g[z].count('A')!=1:
                    flag=False
                    break
            if flag:
                m=max(len(a[i])+2,m)
print(m)