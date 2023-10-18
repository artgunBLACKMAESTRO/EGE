a=[0,1,2,-3,4,5,6]
k=1
for i in range(2,5):
    if a[i]>=0:
        k+=1
        a[k]=a[i]
for i in range(4,len(a)):
    k+=1
    a[k]=a[i]
print(a)