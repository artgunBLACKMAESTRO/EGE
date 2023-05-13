c=0
for a in range(1,1000):
    flag=True
    flag1=False
    for x in range(1,1000):
        flag1 = False
        for z in range(70,81):
            if x%a==0 or ((x%z)<=(x%18!=0)):
                flag1=True
        if not flag1:
            flag=False
            break
    if flag:
        c+=1
print(c)
