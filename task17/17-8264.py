with open('17-8264') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
m=99999999999
for i in range(len(a)):
    m=min(m,abs(a[i]))
b=[]
for i in range(len(a)-1):
    if ((a[i]<0 and a[i+1]>=0) or (a[i]>0 and a[i+1]<0)) and ((a[i]+a[i+1])>0) and ((a[i]+a[i+1])%m==0):
        b.append(a[i]+a[i+1])
print(len(b),max(b))