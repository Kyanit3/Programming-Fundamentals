import math
first_num = int(input())
second_num = int(input())
third_num = int(input())
fourth_num = int(input())

sum = math.floor(first_num+second_num)
devide = math.floor(sum/third_num)
multiply = math.floor(devide*fourth_num)

print(math.floor(multiply))