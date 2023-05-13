with open('24-6636') as f:
    a=f.read()
a=a.replace('3','1')
a=a.replace('5','1')
a=a.replace('4','2')
a=a.replace('21','*')
m=0
c=0
for i in range(len(a)):
    if a[i]=='*':
        c+=1
    else:
        m=max(c,m)
        c=0
print(m,c)