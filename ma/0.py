with open('test') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
k=2
k25=[0]*25
count=0
for i in range(k,len(a)):
    k25[a[i-k]%25]+=1
    count+=k25[(25-a[i]%25)%25]
print(count)
