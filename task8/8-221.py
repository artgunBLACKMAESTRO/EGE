a='ДКМО'
k=0
flag=False
for q in a:
    for w in a:
        for e in a:
            for r in a:
                for i in a:
                    s=q+w+e+r+i
                    if s=='ДОМОК':
                        flag=True
                    if s=='КОМОД':
                        flag=False
                    if flag:
                        k+=1
print(k)