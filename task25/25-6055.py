for i in range(0,10**7,159):
    if str(i)[0]=='2' and str(i)[2]=='1' and ((str(i)[-2]+str(i)[-1]) == '67'):
        print(i,i//159)