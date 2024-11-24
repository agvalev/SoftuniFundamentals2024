n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()

filter_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filter_numbers.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filter_numbers.append(num)
elif command == 'negative':
    for num in numbers:
        if num < 0:
            filter_numbers.append(num)
elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filter_numbers.append(num)
print(filter_numbers)