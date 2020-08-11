team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
red_cards = input().split()
for i in range(len(red_cards)):
    pair = red_cards[i].split("-")
    letter = pair[0]
    num = int(pair[1])

    if letter == "A":
        if num in team_A:
            team_A.remove(num)

    elif letter == "B":
        if num in team_B:
            team_B.remove(num)
    count_A = len(team_A)
    count_B = len(team_B)

    if len(team_A) < 7 or len(team_B) < 7:
        print(f"Team A - {count_A}; Team B - {count_B}")
        print("Game was terminated")
        break

if len(team_B) >= 7 and len(team_A) >= 7:
    print(f"Team A - {count_A}; Team B - {count_B}")
