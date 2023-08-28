with open('9-7335') as f:
    a=f.read()
a=a.split('\n')
a=[list(map(int,a[i].split())) for i in range(len(a))]
qq=0
def test1(b):
    v=(max(b)+min(b))//2
    return (len(set(b)) == len(b)) and (v in b )
def test2(b):
    if len(set(b)) != len(b):
        if len(set(b))==3:
            c=0
            for i in range(len(b)):
                if b[i] in b[i+1:]:
                    c+=2*b[i]**2
                    k=b[i]
                    break
            g=list(set(b))
            g.remove(k)
            return (b[0]**2+b[1]**2)>c
        if len(set(b))==2:
            c=0
            for i in range(len(b)):
                if b[i] not in b[i+1:]:
                    k=b[i]
                    break
            g = list(set(b))
            g.remove(k)
            return (3*b[0]**2)<k**2
        if len(set(b))==1:
            return 0
    else:
        return 0
for i in range(len(a)):
    if (test1(a[i]) and (not test2(a[i]))) or ((not test1(a[i])) and (test2(a[i]))):
        qq+=1
print(qq)