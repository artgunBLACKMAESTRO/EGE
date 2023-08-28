with open('24-ma') as f:
    a=f.read()
s=''
m=0
for i in range(len(a)):
    s+=a[i]
    if '000' in s:
        m=max(m,len(s)-1)
        s='00'
print(len(s),m)