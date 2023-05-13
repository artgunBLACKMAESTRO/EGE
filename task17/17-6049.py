with open('17-6049') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
n=0
for i in range(len(a)):
    if abs(a[i])%10==9:
        n=max(n,a[i])
b=[]
for i in range(len(a)-1):
    if ((abs(a[i])%10==9 and abs(a[i+1])%10!=9) or (abs(a[i+1])%10==9 and abs(a[i])%10!=9)) and ((a[i]**2+a[i+1]**2)<n**2):
        b.append(a[i]**2+a[i+1]**2)
print(len(b),min(b))
