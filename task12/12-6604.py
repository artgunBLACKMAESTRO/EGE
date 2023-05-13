from itertools import permutations as pr


def test(n):
    n = int(n)
    b = set()
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            b.add(i)
            b.add(n // i)
    return len(b) == 3


for m in range(1, 10000):
    q = '>' + 15 * '1' + '2' * 34 + m * '3'
    w = 1 + 15 + 34 + m
    h = set(pr(q, r=w))
    for a in h:
        while '>1' in a or '>2' in a or '>3' in a:
            if '>1' in a:
                a = a.replace('>1', '2>')
            if '>2' in a:
                a = a.replace('>2', '3>')
            if '>3' in a:
                a = a.replace('>3', '11>')
        k = 0
        for i in a:
            if i != '>':
                k += int(i)
        if test(k):
            print(m)
            break
