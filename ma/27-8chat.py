with open('27-8test', 'r') as f:
    n = int(f.readline().strip())
    mod_count = {}
    over_50_count = {}
    for i in range(n):
        num = int(f.readline().strip())
        if num % 80 == 0:
            mod = num % 80
            mod_count[mod] = mod_count.get(mod, 0) + 1
        if num > 50:
            over_50_count[True] = over_50_count.get(True, 0) + 1

count = 0
if '0' in mod_count and '40' in mod_count:
    count = mod_count['0'] * mod_count['40']
elif '0' in mod_count:
    count = mod_count['0'] * (over_50_count.get(True, 0) - mod_count.get('40', 0))
elif '40' in mod_count:
    count = mod_count['40'] * (over_50_count.get(True, 0) - mod_count.get('0', 0))
print(mod_count)
print(count)