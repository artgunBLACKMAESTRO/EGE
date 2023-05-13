for a in range(1,10000):
    flag=True
    for x in range(1,700):
        if (((x%3==0) <=( x%2!=0))or((x-a)>=4)) == 0:
            flag=False
            break
    if flag:
        print(a)