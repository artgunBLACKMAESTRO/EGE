with open('24-17') as f:
    a=f.read()
c=0
k=0
s=''
for i in range(len(a)):
    if a[i]=='A':
        s+=a[i]
        if len(s)>=10 and s.count('B')==0:
            c+=1
        s=''
        s+=a[i]
    else:
        s+=a[i]
print(c)