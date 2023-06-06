for n in range(0,10**8,253):
    if str(n)[:2]=='12' and str(n)[-1]=='6' and str(n)[4:6]=='15':
        print(n,n//253)