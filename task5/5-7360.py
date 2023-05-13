for n in range(1,1000):
    a=bin(n)[2:]
    if len(a)%2==0:
        a=a[:len(a)//2]+'000'+a[len(a)//2:len(a)]
    else:
        a='1'+a+'01'
    if int(a,2)>100:
        print(n)
        break