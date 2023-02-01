for n in range(1,70):
    a=bin(n)[2:]
    for _ in range(3):
        if a.count('1')==a.count('0'):
            a=a+a[-1]
        elif a.count('1')<a.count('0'):
            a=a+'1'
        else:
            a=a+'0'
    if int(a,2)%4==0:
        print(n)
