with open('27-35916') as f:
    a=f.read()
a=a.split('\n')
a=list(map(int,a))
a.pop(0)
m=min(a)
a.remove(m)
n=min(a)
a.remove(n)
b=min(a)
a.remove(b)
ot=m+n+b
l=[9999999999]*3
for i in range(len(a)):
    z=l.copy()
    for n in range(3):
        z[(a[i]%3+n)%3]=min(z[(a[i]%3+n)%3],a[i]+z[a[i]%3])
    l=z
    l[a[i]%3]=min(l[a[i]%3],a[i])
print(ot+l[2])
print(l)