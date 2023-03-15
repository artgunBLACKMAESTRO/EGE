a='1'*84
while '11111' in a:
    a=a.replace('222','1',1)
    a=a.replace('111','2',1)
print(a)