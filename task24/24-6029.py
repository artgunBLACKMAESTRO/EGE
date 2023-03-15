with open('24-6029') as f:
    a=f.read()
a=a.replace('E','1')
a=a.replace('F','2')
while 'DD' in a:
    a=a.replace('DD','D')
a=a.split('D')
c=1
m=0
for i in range(len(a)):
    c=1
    for z in range(len(a[i])-1):
        if (int(a[i][z])%2)!=(int(a[i][z+1])%2):
            c+=1
        else:
            m=max(m,c)
            c=0
    m=max(m,c)
print(m,c)

