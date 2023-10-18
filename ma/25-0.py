for n in range(0,10**9,21):
    if str(n)[0]=='1' and str(n)[-1]=='9' and str(n).count('5')>0:
        flag=True
        for i in range(len(str(n))):