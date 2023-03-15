with open('27-2686B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
minresult=0
D=16
m=[10**10]*D
for i in range(len(a)):
    minresult+=min(a[i])
    diff=(max(a[i])-min(a[i]))
    r=diff%16
    if r!=0:
        mcopy=m.copy()
        for k in range(1,16):
            r0=(r+k)%16
            mcopy[r0]=min(m[r0], m[k]+diff)
        mcopy[r]=min(diff,mcopy[r])
        m=mcopy
if minresult%16!=15:
    print(minresult+m[1])
# A - 6459
# B - 20191039