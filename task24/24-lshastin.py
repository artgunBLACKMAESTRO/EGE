with open('24-lshastin') as f:
    a=f.read()
s=''
m=0
c=0
print(len(a))
for i in range(len(a)):
    if c%20000==0:
        print(c)
    c+=1
    s+=a[i]
    if len(s)>=5 and s[-1]=='D' and s[-4]=='B':
        m=max(m,len(s)-1)
        s=s[-4:]
print(m)