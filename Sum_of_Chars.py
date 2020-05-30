num_of_chars = int(input())
counter = 0
sum = 0
while counter < num_of_chars:
    chars = input()
    sum += ord(chars)
    counter += 1

print(f"The sum equals: {sum}")
