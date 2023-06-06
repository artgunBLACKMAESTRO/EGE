with open('17-8504') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
m=float('inf')
for i in range(len(a)):
    if (len(str(abs(a[i])))==3) and (a[i]%10==5):
        m=min(m,a[i])
b=[]
for i in range(len(a)-1):
    if ((len(str(a[i]))==3) or (len(str(a[i+1]))==3)) and ((a[i]+a[i+1])%m==0):
        b.append(a[i]+a[i+1])
print(len(b),max(b))
