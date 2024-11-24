input_operator = input()
first_num = int(input())
second_num = int(input())

def calculator(input, first, second):
    if input == "multiply":
       return first * second
    elif input == "divide":
        return first / second
    elif input == "add":
        return first + second
    elif input == "subtract":
        return first - second

result = calculator(input_operator, first_num, second_num)

print(result)
