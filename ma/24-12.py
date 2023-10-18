with open('24-12') as f:
    a=f.read()
m=0
c=0
a='APPSSSSPP'
for i in range(len(a)-1):
    if a[i]=='P' and a[i+1]=='P':
        m=max(c,m)
        c=1
    else:
        c+=1
print(m,c)