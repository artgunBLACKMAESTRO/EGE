with open('24-8510') as f:
    a=f.read()
a=a.replace('O','N')
a=a.replace('P','N')
m=0
s=''
for i in range(len(a)):
    s=a[i]
    for j in range(i+1,len(a)):
        s+=a[j]
        if 'NN' in s:
            m=max(m,len(s)-1)
            break
print(m)