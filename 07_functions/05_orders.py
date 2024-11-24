def calculate_price_order(product, count):
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00
    if product == "coffee":
        product = coffee
        return product * count
    elif product == "coke":
        product = coke
        return product * count
    elif product == "water":
        product = water
        return product * count
    elif product == "snacks":
        product = snacks
        return product * count


product_type = input()
count_of_products = int(input())
result = calculate_price_order(product_type, count_of_products)
print(f"{result:.2f}")
