n = int(input())
word = input()
strings = []

for i in range(n):
    curent_string = input()
    strings.append(curent_string)
print(strings)

for az in range(len(strings)- 1, -1,-1):
    element = strings[az]
    if word not in element:
        strings.remove(element)
print(strings)
