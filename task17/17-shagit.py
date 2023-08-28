with open('17-shagit') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
m=99999
for i in a:
    if len(str(i))==4:
        m=min(m,i)
b=[]
for i in range(len(a)-1):
    if ((len(str(a[i]))==4) or (len(str(a[i+1]))==4)) and (a[i]*a[i+1])%m==0:
        b.append(a[i]*a[i+1])
print(len(b),max(b))