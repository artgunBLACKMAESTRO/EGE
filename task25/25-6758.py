for n in range(0,10**8,23):
    if str(n)[0]=='2' and str(n)[-1]=='1' and str(n)[-6:-2]=='5443':
        print(n,n//23)