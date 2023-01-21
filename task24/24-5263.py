
#ABEC, BDAC, CAFB, CFBA,
d='CFBABECAFB'
d=d.replace('ABECAFBDACFBA','****')
d=d.replace('ABECAFBDAC','***')
d=d.replace('CFBABECAFB','***')
d=d.replace('ABECAFB','**')
d=d.replace('ABECFBA','**')
d=d.replace('BDACAFB','**')
d=d.replace('BDACFBA','**')
print(d)