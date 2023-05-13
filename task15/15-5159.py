for a in range(1,1000):
    flag=True
    for x in range(1,100000):
        if (((x%6==0)<=(x%14!=0)) or (((x+a)>=70) and (a%20==0))) == 0:
            flag=False
            break
    if flag:
        print(a)
        break