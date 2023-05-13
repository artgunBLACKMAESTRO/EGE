with open('24-7356') as f:
    a=f.read()
a=a.replace('F','C')
a=a.replace('F','C')
a=a.replace('D','C')
a=a.replace('O','A')
m=0
for i in range(len(a)):
    c=1
    pr=0
    for z in range(i,len(a)-1):
        if a[z]=='C' and a[z+1]=='A':
            pr+=1
        if pr>5:
            m=max(m,c)
            break
        c+=1
print(m)