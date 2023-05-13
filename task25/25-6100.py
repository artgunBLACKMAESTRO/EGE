for i in range(2023*100,10**10,2023):
    l=0
    for k in str(i):
        l+=int(k)
    if str(i)[0]=='1' and str(i)[2]=='1' and str(i)[4]=='1' and str(i)[6]=='1' and str(i)[-1]=='1' and (l==22):
        print(i,i/2023)