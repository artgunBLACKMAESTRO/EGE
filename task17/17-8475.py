with open('17-8475') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
b=[]
ch=float('inf')
for i in range(len(a)):
    if len(str(abs(a[i])))==3 and str(a[i])[-1]=='8':
        ch=min(ch,a[i])
ch=ch**2
b=[]
for i in range(len(a)-2):
    c=[]
    c.append(a[i])
    c.append(a[i+1])
    c.append(a[i+2])
    c.sort()
    if ((c[0]**2<=ch and c[1]**2>ch and c[2]**2>ch) or (c[1]**2<=ch and c[0]**2>ch and c[2]**2>ch) or (c[2]**2<=ch and c[1]**2>ch and c[0]**2>ch))  and ((len(str(abs(c[0])))==3) or (len(str(abs(c[1])))==3) or (len(str(abs(c[2])))==3)):
        print(c)
        b.append(c[0]+c[1]+c[2])
print(len(b),max(b))