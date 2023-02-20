import string

# with open('24-2528') as f:
#     a=f.read()
a='ABDBHSA4152JNNAS6663J88888888'
s='01234556789'
c=''
m=0
for i in range(len(a)):
    if a[i] in s:
        c+=a[i]
    else:
        try:
            if all([int(k)%2==0 for k in c]):
                m=max(m,int(c))
            c=''
        except ValueError:
            continue
print(m,c)
