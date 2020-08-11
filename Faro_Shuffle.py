cards = input().split(" ")
shuffles = int(input())
first_index = cards.pop(0)
last_index = cards.pop(-1)
list_1 = []

for i in range(shuffles):
    first_half = cards[:len(cards)//2]
    second_half = cards[len(cards)//2:]
    for x in range(len(cards)//2):
        list_1.append(second_half[0])
        list_1.append(first_half[0])
        first_half.pop(0)
        second_half.pop(0)
    cards = list_1.copy()
    list_1.clear()  
       
cards.insert(0, first_index)
cards.append(last_index)
print(cards)