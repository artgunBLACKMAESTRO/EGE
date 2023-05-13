m=9999
for n in range(1,1000):
    a=bin(n)[2:]
    if a.count('1')%2==0:
        a='1'+a[2:]+'0'
    else:
        a='11'+a[2:]+'1'
    if 25<int(a,2)<m:
        m=int(a,2)
        ot=n
print(ot)
