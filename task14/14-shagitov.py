x='0123456789ABCDEF'
for i in x:
    a=int('1F3B'+i+'75',16)+int('5D'+i+'3B',16)
    if a%11==0:
        print(a//11)