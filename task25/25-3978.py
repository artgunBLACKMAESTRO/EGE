
for m in range(1,29,2):
    for n in range(0,18,2):
        if 150000000 <= 2**m*3**n <= 300000000:
            print(2**m*3**n,m+n)