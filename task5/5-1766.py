for n in range(100,10000):
    a=bin(n)[2:]
    z=''
    for i in range(len(a)):
        z=a[i]+z
    while z[0]=='0':
        z=z[1:]
    if int(z,2)==9:
        print(n)
        break
