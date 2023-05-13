with open('17-6605') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
m=0
for i in a:
    if i%5==0:
        m=max(m,i)
b=[]
for i in range(len(a)-1):
    if ((a[i]%10==5 and a[i+1]%10!=5) or (a[i+1]%10==5 and a[i]%10!=5)) and (abs(a[i]**2-a[i+1]**2)<=(m**2)):
        b.append(abs(a[i]**2-a[i+1]**2))
print(len(b),max(b))