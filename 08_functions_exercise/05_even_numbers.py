def even(n):
    return n % 2 == 0


numbers = list(map(int, input().split()))

even_numbers = list(filter(even, numbers))
print(even_numbers)
