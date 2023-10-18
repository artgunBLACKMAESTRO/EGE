def f(x,y,z):
    if x>y:
        return 0
    if x==y and ('111' not in z) and ('222' not in z):
        return 1
    if x<y:
        return f(x+1,y,z+'1')+f(x*2,y,z+'2')
    else:
        return 0
print(f(1,16,''))