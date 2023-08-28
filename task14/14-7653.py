a='0123456789ABCDEFGHI'
for i in a:
    z=int('A3'+i+'74',19)+int(i+'40846',19)
    if z%9==0:
        print(z//9)