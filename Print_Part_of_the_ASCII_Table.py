fisrt_char = int(input())
last_char = int(input())
counter = fisrt_char
sum = ''
while counter <= last_char:
    character = chr(counter)
    sum += character + ' '
    counter += 1

print(sum)
