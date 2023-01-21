a='ГЕКЭ023'
c=0
def test1(t:str):
    flag=True
    for i in range(len(t)-1):
        a=set()
        a.add(t[i])
        a.add(t[i+1])
        if len(a) == 1:
            flag=False
            break
    return flag
for q in a:
    for w in a:
        for e in a:
            for r in a:
                t=q+w+e+r
                c+=1
                if (t[0]=='0' or t[0]=='2' or t[0]=='3') and test1(t):
                    print(t, c)
                    break