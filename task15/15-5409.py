c=0
for a in range(1,10000):
    flag=True
    for x in range(1,1000):
        if ((a%25==0) and (((x%24==0) and (x%75==0)) <= (x%a==0))) == 0:
            flag=False
    if flag:
        c+=1
print(c)
