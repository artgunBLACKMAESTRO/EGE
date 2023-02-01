with open('24-3346') as f:
    a=f.read()
a=a.replace('TIK','*')
a=a.replace('TOK','*')
print(a.count('*'))