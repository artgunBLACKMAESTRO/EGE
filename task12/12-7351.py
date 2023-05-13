a=512*'7'
c=0
while '7777' in a or '1111' in a:
    if '7777' in a:
        a=a.replace('7777','1',1)
        c+=1
    else:
        a=a.replace('1111','7',1)
        c+=1
print(c)
