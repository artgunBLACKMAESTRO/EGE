with open('24-8480') as f:
    a=f.read()
a=a.replace('B','A')
a=a.replace('C','A')
s=''
m=0
for i in range(len(a)):
    s+=a[i]
    if 'AA' in s:
        m=max(m,len(s)-1)
        s='A'
print(m)