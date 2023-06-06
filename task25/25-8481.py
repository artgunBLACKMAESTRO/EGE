for n in range(0,10**8,237):
    if str(n)[1:-1].count('9')==0 and str(n)[:2]=='81' and (str(n)[-2]+str(n)[-1])=='80' and str(n)[3]=='2':
        print(n,n//237)