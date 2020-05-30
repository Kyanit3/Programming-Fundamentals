import math
num_people = int(input())
capacity_of_elevator = int(input())

coureses = num_people / capacity_of_elevator

print(math.ceil(coureses))
