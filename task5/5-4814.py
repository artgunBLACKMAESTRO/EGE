for n in range(1,10**8):
    s1=0
    s2=0
    n=str(n)
    for i in range(len(n)):
        if int(n[i])%2==0:
            s1+=int(n[i])
    for i in range(len(n)-1,-1,-2):
        s2+=int(n[i])
    q=abs(s1-s2)
    if q==26:
        print(n)
        break
