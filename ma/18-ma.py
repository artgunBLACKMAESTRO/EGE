with open('18-ma') as f:
    a=f.read()
a=a.split('\n')
a=[float(i.replace(',','.')) for i in a]
c=0
m=0
for i in range(len(a)-1):
    c=a[i]
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j])<=8:
            c+=a[j]
        else:
            break
    m=max(c,m)
print(m)
