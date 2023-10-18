# with open('24-stat') as f:
#     a=f.read()
m=0
a='HHDOOMMMDOOMDOOOKLD'
for i in range(len(a)):
    if a[i]=='D':
        c=1
        b=i
        pr=0
        s=''
        k=0
        while b!=(len(a)-1):
            b+=1
            c+=1
            if a[b]=='O':
                pr+=1
            elif a[b]=='D' and pr<=2:
                pr=0
                k+=c
                c=0
                m=max(m,k)
            if pr==3:
                m=max(m,k)
                break
print(m)
