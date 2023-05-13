a='4'*9+'5'*(21-9)
while '444' in a or '888' in a:
    if '444' in a:
        a=a.replace('444','8',1)
    if '555' in a:
        a=a.replace('555','8')
    if '888' in a:
        a=a.replace('888','3')
print(a)