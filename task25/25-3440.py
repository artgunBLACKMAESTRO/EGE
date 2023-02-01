b=[]
for n in range(33333,55556):
    flag=True
    for x in range(2,int(n**(0.5))+1):
        if n%x==0:
            flag=False
            break
    c=0
    n=str(n)
    for i in range(len(n)):
        c+=int(n[i])
    if flag and c>35:
        print(n,c)