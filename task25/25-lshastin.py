def deli(n):
    s=set()
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
for n in range(5*10**5,10**6+1):
    b=deli(n)
    c=0
    if b:
        for i in b:
            if len(str(i))==4 and str(i)[-1]=='0':
                c+=1
    if c>45:
        print(n,c)