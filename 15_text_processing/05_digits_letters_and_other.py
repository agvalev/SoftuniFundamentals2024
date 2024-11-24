text = input()
numbers = ""
letters = ""
charachters = ""

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        charachters += char


print(numbers)
print(letters)
print(charachters)