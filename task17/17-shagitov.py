with open('17-shagitov') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
m=0
for i in a:
    if len(str(i))==3:
        m=max(m,i)
b=[]
for i in range(len(a)-1):
    if ((len(str(a[i]))==3 and len(str(a[i+1]))!=3) or (len(str(a[i+1]))==3 and len(str(a[i]))!=3)) and (a[i]+a[i+1])%m==0:
        b.append(a[i]+a[i+1])
print(len(b),max(b))