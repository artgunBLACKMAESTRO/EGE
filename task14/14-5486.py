x='0123456789abcdefghi'
for i in x:
    m='55'+i+'36'
    n=i+'2724'
    q=int(m,19)+int(n,19)
    if q%11==0:
        print(q/11)
        break