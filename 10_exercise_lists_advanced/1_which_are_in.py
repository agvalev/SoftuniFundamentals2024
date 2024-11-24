first_sequens = input().split(", ")
second_sequens = input().split(", ")

substrings = []
for first_string in first_sequens:
    for second_string in second_sequens:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)

