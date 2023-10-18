with open('17-29') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
n=0
for i in range(len(a)):
    if abs(a[i])%10==6:
        n=min(n,a[i])
b=[]
for i in range(len(a)-1):
    if ((abs(a[i])%10==6 and abs(a[i+1])%10!=6) or (abs(a[i+1])%10==6 and abs(a[i])%10!=6)) and ((a[i]**2+a[i+1])<n**2):
        b.append(a[i]**2+a[i+1]**2)
print(len(b),max(b))