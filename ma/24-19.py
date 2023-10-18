with open('24-19') as f:
    a=f.read()
c=0
k=0
s=''
for i in range(len(a)):
    if a[i]=='D':
        s+=a[i]
        if len(s)>=10 and s.count('C')>=2:
            c+=1
        s=''
        s+=a[i]
    else:
        s+=a[i]
print(c)