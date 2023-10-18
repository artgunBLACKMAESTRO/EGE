with open("27-13A", "r") as file:
    nums=file.readlines()
nums=list(map(int,nums))
# создаем три списка чисел, которые дают остатки 0, 1, 2 при делении на 3
r0, r1, r2 = [], [], []
for num in nums:
    if num % 3 == 0:
        r0.append(num)
    elif num % 3 == 1:
        r1.append(num)
    else:
        r2.append(num)

# сортируем списки по убыванию
r1.sort(reverse=True)
r2.sort(reverse=True)
r0.sort(reverse=True)

# выбираем максимальную сумму
max_sum = 0
if len(r0) >= 3:
    max_sum = sum(r0[:3])
if len(r0) == 2:
    max_sum = max(max_sum, sum(r0) + max(r1[:2] + r2[:2]))
if len(r0) == 1:
    max_sum = max(max_sum, sum(r0) + max(r1[:3] + r2[:3]))
if len(r0) == 0:
    max_sum = max(max_sum, sum(r1[:3]) + sum(r2[:3]))
print(max_sum)