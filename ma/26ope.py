with open('26-ma', 'r') as f:
    n = int(f.readline().strip())
    nums = [int(f.readline().strip()) for _ in range(n)]

evens = set(filter(lambda x: x % 2 == 0, nums))
odds = set(filter(lambda x: x % 2 == 1, nums))

pairs = set((a, b) for a in evens for b in odds if a + b in nums)

max_sum = max([sum(pair) for pair in pairs])

count_pairs = len(pairs)

with open('output.txt', 'w') as f:
    f.write(str(count_pairs) + '\n')
    f.write(str(max_sum) + '\n')