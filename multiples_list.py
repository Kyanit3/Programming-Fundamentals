factor = int(input())
count = int(input())
list_1 = []
kurec = 0
for x in range (0, count):
    kurec += factor
    list_1.append(kurec)

print(list_1)