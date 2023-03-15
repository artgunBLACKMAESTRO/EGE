with open('24-6757') as f:
    a=f.read()
a=a.replace('CFE','*')
a=a.replace('FCE','*')
m=0
c=0
for i in range(len(a)):
    if a[i]=='*':
        c+=1
    else:
        m=max(m,c)
        c=0
print(m)