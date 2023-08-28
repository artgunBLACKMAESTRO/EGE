import fnmatch
c=0
for i in range(111*6,10**7,111):
    if str(i)[:2]=='22' and str(i)[3]=='0' and str(i)[-2]=='5':
        print(i,i//111)