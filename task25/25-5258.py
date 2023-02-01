for i in range(103,10**10,103):
    n=str(i)
    flag=True
    for z in range(len(n)-1):
        if n[z]>=n[z+1]:
            flag=False
    if flag:
        print(i, i/103)