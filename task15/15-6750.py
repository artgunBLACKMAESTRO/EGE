for a in range(10000):
    flag=True
    for x in range(1,1000):
        if not flag:
            break
        for y in range(1,1000):
            if (((x+y)<=32)or(y<=(x+4))or(y>=a))==0:
                flag=False
                break
    if flag:
        print(a)