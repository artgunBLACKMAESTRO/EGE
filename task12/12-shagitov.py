c=0
for p in range(1000,2001):
    a='7'+p*'8'
    while '78' in a or '888' in a:
        if '78' in a:
            a=a.replace('78','8',1)
        if '888' in a:
            a=a.replace('888','7',1)
    m=0
    for i in a:
        m+=int(i)
    if m==16:
        c+=1
print(c)