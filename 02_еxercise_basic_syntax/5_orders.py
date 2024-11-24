
number_of_orders = int(input())
price = 0
total_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    if price_per_capsule <0.01 or price_per_capsule > 100.00:
        continue

    price_day = price_per_capsule * capsules_per_day
    price = price_day * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")


#moje i da satne if proverkite sushto sus if capsulse not in range(1, 31 +1/32)