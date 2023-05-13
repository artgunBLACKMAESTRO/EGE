b=[]
for i in range(0,10**10,53191):
    if str(i)[1:4]=='136' and (int(str(i)[0])%2==0):
        if len(str(i))>4:
            if int(str(i)[-1])%2==1:
                b.append(i)
        else:
            b.append(i)
b.sort(reverse=True)
for i in range(5):
    print(b[i],b[i]//53191)