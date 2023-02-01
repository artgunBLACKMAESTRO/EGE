m=0
for n in range(1,101):
    k=n
    n=bin(n)[2:]
    while len(n)!=8:
        n='0'+n
    n=n[:-1]
    z=''
    for i in range(len(n)):
        z=n[i]+z
    if int(z,2)==k:
        print(k)