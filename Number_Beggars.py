numbers = input().split(", ")
numbers = map(int, numbers)
numbers = list(numbers)
baggers = int(input())
index = 0
baggers_count = []
for i in range(baggers):
    baggers_count.append(0)

for numbers in numbers:
    baggers_count[index] += numbers
    index += 1
    if index >= baggers:
        index = 0

print(baggers_count)