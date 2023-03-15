with open('24-18') as f:
    a=f.read()
a=a.replace('C','B')
i=0
c=0
m=0
while i <= (len(a)-1):
    if a[i] == 'A' and a[i+1] == 'B':
        c+=1
        i+=1
    else:
        m=max(m,c)
        c=0
    i+=1
print(m,c)