for n in range(0,10**10,3052):
    if str(n)[0]=='1' and str(n)[2:6]=='2139' and str(n)[-1]=='4':
        print(n,n//3052)