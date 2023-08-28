m=0
for a in range(1,10000):
    flag=True
    for x in range(1,1000):
        if ((x%17==0) <= ((not(80 <= x <= 100)) or (a<x+30))) == 0:
            flag=False
            break
    if flag:
        m=max(m,a)
print(m)