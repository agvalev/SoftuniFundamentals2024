def positiv(list):
    return ", ".join([number for number in list if int(number) >=0])


def negativ(list):
    return ", ".join([number for number in list if int(number) < 0])


def even(list):
    return ", ".join([number for number in list if int(number) % 2 == 0])


def odd(list):
    return ", ".join([number for number in list if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positiv(numbers)}")
print(f"Negative: {negativ(numbers)}")
print(f"Even: {even(numbers)}")
print(f"Odd: {odd(numbers)}")