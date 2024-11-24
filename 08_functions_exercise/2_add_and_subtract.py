def add_add_subtract():
    def sum_numbers(num1, num2):
        return num1 + num2

    def subtract(summed_numbers, num3):
        return summed_numbers - num3

    result = sum_numbers(num1, num2)
    print(subtract(result, num3))


num1 = int(input())
num2 = int(input())
num3 = int(input())

# result = sum_numbers(num1, num2)
# print(subtract(result, num3))
add_add_subtract()
