# number_list = input().split()
#
# absolute_currency = []
#
# for number in number_list:
#     absolute_currency.append(abs(float(number)))
#
# print(absolute_currency)

number_list = input().split()

absolute_currency = [abs(float(number)) for number in number_list]
