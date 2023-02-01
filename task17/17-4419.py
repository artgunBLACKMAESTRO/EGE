def test(x:int):
    return (x>0) and (len(str(x)) == 2) and (x%2==1)
with open('17-4419') as f:
    a=f.readlines()
a=list(map(int,a))
b=[]
for i in range(len(a)-2):
    if (test(a[i]) == 0) and (test(a[i+1])) and (test(a[i+2]) == 0):
        b.append(a[i]+a[i+1]+a[i+2])
print(len(b),max(b))