def even_or_odd(number):
    even_numbers = 0
    odd_numbers = 0
    for i in number:
        i = int(i)
        if i % 2 == 0:
            even_numbers += i
        else:
            odd_numbers += i
    print(f"Odd sum = {odd_numbers}, Even sum = {even_numbers}")


numbers = input()

even_or_odd(numbers)



