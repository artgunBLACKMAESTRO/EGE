for n in range(1,9):
    a=bin(n)[2:]
    if a[-1]=='0':
        a='10'+a
    else:
        a='1'+a+'01'
    print(int(a,2))