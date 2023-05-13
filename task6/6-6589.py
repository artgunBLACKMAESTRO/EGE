from math import sqrt as s
k=0
for y in range(16):
    for x in range(14):
        if x>0 and y>(1/s(3)*x) and y<((-1/s(3))*x+16):
            print((x,y))
            k+=1
print(k)