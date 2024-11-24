def facuriel(n):
    if n == 0:
        return 1
    else:
        return n* facuriel(n-1)
def factoriel_div(num1, num2):
    result = facuriel(num1)
    result2 = facuriel(num2)
    division_result = result / result2
    return f"{division_result:.2f}"

first = int(input())
second = int(input())
print(factoriel_div(first, second))
