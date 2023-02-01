for x in range(2,10):
    s=''
    b=30
    while b!=0:
        s=str(b%x)+s
        b=b//x
    if len(s)==3:
        print(x)
        break