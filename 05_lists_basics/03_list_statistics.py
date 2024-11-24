n = int(input())

p_numbers = []
n_numbers = []

for _ in range(n):
    number = int(input())

    if number > 0:
        p_numbers.append(number)
    else:
        n_numbers.append(number)
print(p_numbers)
print(n_numbers)
print(f"Count of positives: {len(p_numbers)}")
print(f"Sum of negatives: {sum(n_numbers)}")

print(len(p_numbers))