for a in range(0,100):
    flag=True
    for x in range(500):
        if (((x&52!=0)and(x&36==0))<=(x&a!=0)) == 0:
            flag=False
            break
    if flag:
        print(a)
        break