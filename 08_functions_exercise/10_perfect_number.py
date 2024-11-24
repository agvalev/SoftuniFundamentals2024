def is_perfect_number(number):
    divisors_sum = sum(divisior for divisior in range(1, number)if number % divisior == 0)
    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."



number = int(input())
print(is_perfect_number(number))