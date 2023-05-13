print('a b c ans')
for a in range(2):
    for b in range(2):
        for c in range(2):
            k=((a and b) or (c and((not a)or b))) == 1
            print(a,b,c,k)