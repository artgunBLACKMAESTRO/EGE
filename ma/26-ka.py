n, m = map(int, input().split())  # считываем первую строку

sum_a = 0  # сумма всех изделий А
with open('26-ma', 'r') as f:
    for i in range(n):
        price, cnt, item_type = f.readline().split()
        price, cnt = int(price), int(cnt)
        if item_type == 'А':
            sum_a += price * cnt

sum_b = m - sum_a  # вычисляем сумму, которую можно потратить на изделия В
cnt_b = 0  # количество изделий В, которое можно купить за оставшуюся сумму
with open('26-ma', 'r') as f:
    next(f)  # пропускаем первую строку
    for line in f:
        price, cnt, item_type = line.split()
        price, cnt = int(price), int(cnt)
        if item_type == 'В' and price <= sum_b:
            cnt_b += cnt
            sum_b -= price * cnt

print(cnt_b, sum_b)