for a in range(1,1000):
    flag=True
    for x in range(1,1000):
        if ( ((x%3==0) <= (x%5!=0)) or ((x+a)>=70) ) == 0:
            flag=False
            break
    if flag:
        print(a)
        break