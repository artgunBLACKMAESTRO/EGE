from itertools import product as pr
a=pr('АКЛМРС',repeat=6)
z='АКЛМРС'
c=0
for i in a:
    j=''.join(i)
    c+=1
    pr=0
    flag=True
    r=0
    if 'КС' not in j and 'СК' not in j:
        for k in z:
            pr=j.count(k)
            if pr>1 and pr!=3:
                flag=False
                break
            if pr==3:
                r+=1
    if flag and r==1:
        print(j,c)