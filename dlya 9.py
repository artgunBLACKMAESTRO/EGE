a = [5, 3, 9, 5, 6]


# 1 способ (прямой)
unique = []
non_unique = []
for i in a:
    if a.count(i) > 1:
        non_unique.append(i)
    else:
        unique.append(i)

print(non_unique, unique)

# 2 способ (списочные выражения)
unique = []
non_unique = []
[non_unique.append(i) if a.count(i) > 1 else unique.append(i) for i in a]

print(non_unique, unique)