number_of_lines = int(input())

water_tank_capacity = 255

for liters in range(number_of_lines):
    liters_in_tank = int(input())
    if water_tank_capacity - liters_in_tank <0:
        print("Insufficient capacity!")
        continue
    water_tank_capacity -= liters_in_tank
print(255-water_tank_capacity)




#     water_tank_capacity -= liters_in_tank
#     if water_tank_capacity <= 0:
#         print("Insufficient capacity!")
# print(abs(water_tank_capacity))

