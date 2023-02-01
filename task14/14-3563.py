c=0
for x in range(17,10000):
    m=oct(x)[2:]
    n=hex(x)[2:]
    if len(m)==3 and (m)[1]=='0' and len(n)==2 and (n)[-1]==5:
        c+=1
print(c)