with open('24-5387') as f:
    a=f.read()
a=a.replace('B','A')
a=a.replace('C','A')
a=a.replace('2','1')
a=a.replace('3','1')
a=a.replace('A1','*')
c=0
m=0
for i in range(len(a)):
    if a[i]=='*':
        c+=1
    else:
        m=max(m,c)
        c=0
print(m)
