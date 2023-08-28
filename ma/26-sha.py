def freerooms(rooms, time):
    ans = 0
    for room in rooms:
        if room < time:
            ans += 1
    return ans

f = open("26-sha")
k = int(f.readline())
n = int(f.readline())
a = [list(map(int, i.split())) for i in f.readlines()]
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i][0] > a[j][0]:
            a[i], a[j] = a[j], a[i]
        elif a[i][0] == a[j][0]:
            if a[i][2] > a[j][2]:
                a[i], a[j] = a[j], a[i]
            elif a[i][1] > a[j][1]:
                a[i], a[j] = a[j], a[i]
rooms = [0] * k
ans1 = 0
timer = 0
people = 0
for member in a:
    if freerooms(rooms, member[0]) >= member[2]:
        count = 0
        room_number = 0
        ans1 += 1
        people += member[2]
        while count < member[2]:
            if rooms[room_number] < member[0]:
                count += 1
                rooms[room_number] = member[1]
                room_number += 1
        if freerooms(rooms, member[0]) == 0:
            timer += min(rooms) - member[0] + 1
print(a)
print(ans1, 1440 - timer)