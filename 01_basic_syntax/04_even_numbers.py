chislo = int(input())

for i in range(chislo):
    n = int(input())
    if n % 2 != 0:
        print(f"{n} is odd!")
        break
else:
    print("All numbers are even.")