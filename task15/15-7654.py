C=[x for x in range(30,46)]
for a in range(1,1000):
    flag=True
    for x in range(1,500):
        if (((x%a==0) and (x in C)) <= (x%12!=0)) == 0:
            flag=False
            break
    if flag:
        print(a)
        break