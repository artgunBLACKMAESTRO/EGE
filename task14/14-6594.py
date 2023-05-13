for x in range(3,4):
    a=int('753'+str(x)+'2',13)+int('2'+str(x)+'173',13)
    if a%12==0:
        print(a/12)