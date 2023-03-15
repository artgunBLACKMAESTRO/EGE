for n in range(1,101):
    a=bin(n)[2:]
    v=''
    for i in a:
        v=i+v
    v=str(int(v))
    if int(v,2)==11:
        print(n)