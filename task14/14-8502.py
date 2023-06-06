a='0123456789ABCDE'
for x in a:
    c=int('99658'+x+'29',15)+int('102'+x+'023',15)
    if c%14==0:
        print(c/14)