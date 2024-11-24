# number = int(input())
#
# for cur_number in range(1,number+1):
#     cur_number_string = str(cur_number)
#     digit_sum = 0
#     for digit in cur_number_string:
#         digit_sum += int(digit)
#     if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
#         print(f"{cur_number} -> True")
#     else:
#         print(f"{cur_number} -> False")
#
#
number = int(input())
for cur_number in range(1,number+1):
    cur_number_string = str(cur_number)
    digit_sum = 0
    for digit in cur_number_string:
        digit_sum += int(digit)
        is_special = False
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
    print(f"{cur_number} -> {is_special}")


