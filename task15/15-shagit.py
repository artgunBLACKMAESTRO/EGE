for b in range(1000):
    flag=True
    for x in range(1000):
        if (((x&500!=0) and (x&200==0)) <= (not(x&b==0))) == 0:
            flag=False
            break
    if flag:
        print(b)
        break