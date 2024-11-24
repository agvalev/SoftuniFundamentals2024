list_strings = input().split()

number = int(input())
list_int = [int(x) for x in list_strings]

for _ in range(number):
    smallest_num = min(list_int)
    list_int.remove(smallest_num)

list_int = [str(x) for x in list_int]
x = ", ".join(list_int)
print(x)

