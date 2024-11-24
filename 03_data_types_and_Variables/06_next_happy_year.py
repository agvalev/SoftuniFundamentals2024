# years = int(input())
#
# while True:
#     years += 1
#     is_year = True
#     alredy_found_d = ""
#     for digit in str(years):
#         if digit in alredy_found_d:
#             is_year = False
#             break
#         alredy_found_d += digit
#     if is_year:
#         break
# print(years)

years = int(input())

while True:
    years += 1
    year_as_string = str(years)
    if len(year_as_string) == len(set(year_as_string)):
        break
print(years)
