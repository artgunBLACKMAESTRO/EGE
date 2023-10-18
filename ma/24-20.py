a=open('24-20')
d=a.read()
d=d.replace('A','*')
d=d.replace('B','*')
m=0
for i in range(len(d)):
    k=0
    j=i
    l=0
    while k<=3 and len(d)!=j:
        if d[j]=='*':
            k+=1
        if k!=4:
            l+=1
        j+=1
    m=max(l,m)
print(m)