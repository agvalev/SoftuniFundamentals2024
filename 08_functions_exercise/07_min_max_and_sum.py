def min_max_sum(n):
    min_number = min(n)
    max_number = max(n)
    sum_number = sum(n)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_number}")


numbers = list(map(int, input().split()))
min_max_sum(numbers)
