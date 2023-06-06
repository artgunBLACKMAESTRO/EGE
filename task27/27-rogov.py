with open('27-rogova') as f:
    a=f.read().strip()
a=list(map(int,a.split('\n')))
k=a.pop(0)
a.pop(0)
c=0
tek=0
sum=0
for i in range(k,len(a)):
    tek=max(tek,a[i-k])
    if a[i-k]%26==0:
        c=max(c,a[i-k])
    if a[i]%26==0 and abs(a[i]-tek)%2==1:
        sum=max(sum,a[i]+tek)
    if abs(a[i] - c) % 2 == 1:
        sum=max(sum, a[i] +c)
print(sum)


