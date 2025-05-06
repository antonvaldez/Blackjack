import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def value_computer():
    return sum(computer)

def value_player():
    return sum(player)

def winner():
    print(f"    Your final hand: {player}, final score: {value_player()}")
    while value_computer() <= 16:
        computer.append(random.choice(cards))
        while 11 in computer and value_computer() > 21:
            computer[computer.index(11)] = 1
    final_score_computer = value_computer()
    print(f"    Computer's final hand: {computer}, final score: {final_score_computer}")
    if final_score_computer == 21 and len(computer) == 2:
        print("    😭 Computer hit Blackjack!. You lose!")
    elif final_score_computer > 21:
        print("    🏆 Computer went over. You win!")
    else:
        if final_score_computer > value_player():
            print("     😭 You lose!")
        elif final_score_computer == value_player():
            print("    🫰 It is a draw!")
        else:
            print("    🏆 You Win!")

def next_round():
    player.append(random.choice(cards))
    while 11 in player and value_player() > 21:
        player[player.index(11)] = 1
    print(f"    Your cards: {player}, current score: {value_player()}")
    print(f"    Computer's first card: {computer}")
    if value_player() > 21:
        print("    😭 You went over. You lose!")
    else:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            next_round()
        else:
            winner()

def start_game():
    print("\n" * 100)
    print(r"""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """)
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    computer.append(random.choice(cards))
    print(f"    Your cards: {player}, current score: {value_player()}")
    print(f"    Computer's first card: {computer}")
    if value_player() == 21:
        print("    🏆 You hit Blackjack!. You win!")
    else:
        choice = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            next_round()
        else:
            winner()

while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    player = []
    computer = []
    start_game()
print("\n\nThank you for playing!")
