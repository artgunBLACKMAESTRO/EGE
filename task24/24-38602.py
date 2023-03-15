with open('24-38602') as f:
    a=f.read()
m=0
c=1
for i in range(len(a)-1):
    if a[i]=='P' and a[i+1]=='P':
        m=max(m,c)
        c=1
    else:
        c+=1
print(m,c)