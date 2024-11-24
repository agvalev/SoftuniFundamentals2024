group_size = int(input())
days = int(input())
coins = 0
for cur_day in range(1, days+1):
    if cur_day % 10 == 0:
        group_size -= 2

    if cur_day % 15 ==0:
        group_size += 5

    if cur_day % 3 == 0:
        coins -= 3 * group_size

    if cur_day % 5 == 0:
        coins += 20 * group_size
        if cur_day % 3 == 0:
            coins -= 2*group_size

    coins += 50
    coins -= 2 * group_size
    coins_per_companion = coins // group_size
print(f"{group_size} companions received {coins_per_companion} coins each.")