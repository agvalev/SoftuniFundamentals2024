numbers = list(map(int, input().split(', ')))
neshto = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))

even = list(filter(lambda a: a != 'no', neshto))
print(even)
