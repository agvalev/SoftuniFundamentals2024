pnumber = int(input())
second_number = int(input())

for number in range(second_number, pnumber, -1):
    if number % pnumber == 0:
        print(number)
        break
#vajno!!!

