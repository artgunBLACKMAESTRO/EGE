def deli(n):
    b=set()
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            b.add(i)
            b.add(n//i)
    return list(b)
j=0
for i in range(500000,10**8):
    k=[]
    v=deli(i)
    for z in v:
        if z!=8 and z%10==8:
            k.append(z)
    if len(k)>0:
        print(i,min(k))
        j+=1
        if j==5:
            break
