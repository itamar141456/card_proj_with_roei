from player_class import Player
from Card_Game import CardGame

# game setup: 2 players, cards to deal for each
player1_name = input("enter player 1 name")
while player1_name == "":
    player1_name = input("invalid! enter player 1 name: ")
player2_name = input("enter player 2 name: ")
while player2_name == "" or player2_name == player1_name:
    player2_name = input("invalid, enter a different name for player 2: ")
num_game_cards = input("enter a number of cards to deal to each player, for the default(10) press enter: ")
while not num_game_cards.isnumeric() and not num_game_cards == "":
    num_game_cards = input(
        "invalid, use numbers! enter a number of cards to deal to each player, for default(10) press "
        "enter: ")

player1 = Player(player1_name)
player2 = Player(player2_name)
if num_game_cards == "":
    main_game = CardGame(player1, player2)
else:
    main_game = CardGame(player1, player2, int(num_game_cards))
print(f"\n{player1}\n")
print(f"{player2}")

# game is starting, 10 rounds (a break if one of the players dropped all the cards)
for round_number in range(1, 11):
    if not len(player1.hand) == 0 and not len(player2.hand) == 0:
        print("")
        print(f"---------------- roound {round_number} - fight ----------------")
        player1_card = player1.get_card()
        print(f"{player1.name} card: {player1_card}")
        player2_card = player2.get_card()
        print(f"{player2.name} card: {player2_card}")
        if player1_card > player2_card:
            player2.add_cards(player1_card)
            player2.add_cards(player2_card)
            print(f"{player1.name} is the winner of round {round_number}")
        elif player2_card > player1_card:
            player1.add_cards(player2_card)
            player1.add_cards(player1_card)
            print(f"{player2.name} is the winner of round {round_number}")
    else:
        break

# game is finished. results:
if main_game.get_winner() == None:
    print("The game ended in a draw")
else:
    print(f"\n{main_game.get_winner().name} is the undisputed champion!!!")
