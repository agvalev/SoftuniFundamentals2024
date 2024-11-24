foods_and_q = input().split()
final_products = {}
for index in range(0, len(foods_and_q), 2):
    product = foods_and_q[index]
    quantity = int(foods_and_q[index + 1])
    #do tuk gi razdewlqme


    final_products[product] = quantity
    #tuk gi slagame v dicta


print(final_products)