def rounding(a):
    return round(a)


numbers = input().split()


numbers = [float(x) for (x) in numbers]
numbers = [rounding(x) for (x) in numbers]



print(numbers)

# print(result)
