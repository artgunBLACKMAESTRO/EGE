with open('24-7662') as f:
    a=f.read()
c=3
m=0
for i in range(3,len(a)):
    flagcif=set()
    flagSOLO=0
    for z in range(i,len(a)):
        if a[z]=='O' and a[z-1]=='L' and a[z-2]=='O' and a[z-3]=='S':
            flagSOLO+=1
        if a[z] in '0123456789':
            flagcif.add(a[z])
        if flagSOLO>4 and len(flagcif)>=5:
            m=max(c,m)
            c=3
            break
        c+=1
print(m)