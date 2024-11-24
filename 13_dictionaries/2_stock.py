foods_and_q = input().split()
serched_products = input().split()
final_products = {}
for index in range(0, len(foods_and_q), 2):
    product = foods_and_q[index]
    quantity = int(foods_and_q[index + 1])
    final_products[product] = quantity # dobavqm go v rechnika


for product in serched_products:
    if product in final_products.keys():
        print(f"We have {final_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
