def deli(n):
    s=set()
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    if s:
        return sum(list(s))
    else:
        return 0
def prost(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True
c=0
for i in range(1273548,10**9):
    m=deli(i)
    if m!=0:
        if prost(m%100000):
            print(i,m)
            c+=1
            if c==5:
                break