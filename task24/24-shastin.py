with open('24-shastin') as f:
    a=f.read()
m=0
s=''
a=a.replace('F','A')
a=a.replace('E','A')
a=a.replace('D','A')
a=a.replace('C','A')
a=a.replace('B','A')
for i in range(len(a)):
    s+=a[i]
    if 'AAA' in s:
        m=max(m,len(s)-1)
        s='AA'
print(m)
