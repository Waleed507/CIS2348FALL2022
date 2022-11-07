# Waleed Yusuf
# 2104654

players = {}

for i in range(5):
    jersey_num = int(input(f"Enter player {i+1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i+1}'s rating:\n\n"))

    players[jersey_num] = rating
print("ROSTER")
for key, value in sorted(players.items()):
    print('Jersey number: %d, Rating: %d' % (key, value))
print("\nMENU")
player_input = input("a - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n\nChoose an option:\n")

while player_input != 'q':
    if player_input == 'o':
        continue
    elif player_input == 'a':
        jersey_num = int(input(f'\nEnter a new player\'s jersey number:\n'))
        rating = int(input(f'Enter the player\'s rating:\n'))
        players[jersey_num] = rating
    elif player_input == 'd':
        del_player = int(input(f'\nEnter a jersey number:\n'))
        del players[del_player]

    elif player_input == 'u':
        new_jersey = int(input('Enter a jersey number: \n'))
        new_rating = int(input('Enter a new rating for player: \n'))
        players.update({new_jersey: new_rating})

    print("MENU")
    player_input = input("a - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n\nChoose an option:\n")
