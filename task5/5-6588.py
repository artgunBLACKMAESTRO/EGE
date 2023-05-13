for n in range(10, 1000):
    a = bin(n)[2:]
    j = ''
    for i in range(len(a)):
        if a[i]=='1':
            j+='0'
        else:
            j+='1'
    j = '1' + j
    if j.count('1') % 2 == 0:
        j = j + '0'
    else:
        j = j + '1'
    if int(j, 2) > 180:
        print(n)
        break
