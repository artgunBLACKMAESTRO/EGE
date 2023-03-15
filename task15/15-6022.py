for a in range(1000):
    flag = True
    for x in range(1000):
        if not flag:
            break
        for y in range(1000):
            if ((x < a) or (y < a) or ((x + 2 * y) > 150)) == 0:
                flag = False
                break
    if flag:
        print(a)
        break
