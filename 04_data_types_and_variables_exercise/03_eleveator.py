import math

persons_in_elevator = int(input())
capacity = int(input())

courses = math.ceil(persons_in_elevator / capacity)

print((courses))

