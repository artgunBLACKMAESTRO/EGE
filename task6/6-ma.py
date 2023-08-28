c=0
for x in range(123):
    for y in range(124):
        if x>0 and (y<(-(1/(3**(1/2)))*x+123)) and (y>((1/(3**(1/2)))*x)):
            c+=1
print(c)