for n in range(129*10,10**8,129):
    if str(n)[:2]=='12' and str(n)[3]=='3' and (str(n)[-2]+str(n)[-1]) == '46':
        print(n,n//129)