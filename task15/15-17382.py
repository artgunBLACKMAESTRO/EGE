for a in range(1000):
    flag=True
    for x in range(1000):
        if not flag:
            break
        for y in range(1000):
            if (((5*x+3*y) !=60)or((a>x)and(a>y))) == 0:
                flag=False
                break
    if flag:
        print(a)
        break