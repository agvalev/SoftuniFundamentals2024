total_price = 0
total_taxes = 0
price_without_taxes = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break
    each_price = float(command)
    if each_price <= 0:
        print("Invalid price!")
        continue
    price_without_taxes += each_price

total_taxes = price_without_taxes * 0.2
total_price = total_taxes + price_without_taxes
if command == "special":       #dori inputa pazi sobstvenata si stojnost
    total_price = total_price - (total_price * 0.1) # total price - 10% ot nego (:
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print(f"Total price: {total_price:.2f}$")
    print("-----------")
