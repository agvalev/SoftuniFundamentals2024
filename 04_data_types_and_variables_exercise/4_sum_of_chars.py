n_cikul = int(input())

total_sum = 0

for l_p_l in range(n_cikul):
    letter = input()
    total_sum += ord(letter)
print(f"The sum equals: {total_sum}")
