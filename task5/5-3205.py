for n in range(2,1000):
    a=bin(n)[2:]
    a=a+a[-2]
    a=a+a[1]
    if int(a,2)>210:
        print(n)
        break