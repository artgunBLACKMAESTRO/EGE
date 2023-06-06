for n in range(1,1000):
    a=bin(n)[2:]
    if n%3==0:
        a=a+a[-3:-1]+a[-1]
    else:
        a=a+bin((n%3)*3)[2:]
    if int(a,2)<76:
        print(n)