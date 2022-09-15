import random
player = int(input("please input a number between(including) 1-5: "))-1
opponent = random.randint(0,4)
order = ['rock', 'scissors', 'lizard', 'paper', 'spock']
print(f"you picked {order[player]}")
print(f"your opponent picked {order[opponent]}")
if player == opponent:
    print("draw")
elif player == 0 and opponent == 1 or player == 0 and opponent == 2:
    print("win")
elif player == 1 and opponent == 2 or player == 1 and opponent == 3:
    print("win")
elif player == 2 and opponent == 3 or player == 2 and opponent == 4:
    print("win")
elif player == 3 and opponent == 4 or player == 3 and opponent == 0:
    print("win")
elif player == 4 and opponent == 0 or player == 4 and opponent == 1:
    print("win")
else:
    print("lose")

# elif player != opponent:
#     for times in range(0,5):
#         if player == times and opponent == times+1 or player == times+2:
#             print("win")
#     for times in range(0,5,-1):
#         if player == times and opponent == times+1 or player == times+2:
#             print("win")


# if player == opponent:
#     print("Draw")
# else:
#     for times in range(0,5):
#         print(times)
#         if opponent-player == times:
#             print("win")
#             break
#         if player-opponent == times:
#             print("lose")
#             break

# elif opponent-player == 1 or opponent-player == 2:
#     print("win")
# elif player-opponent == 1 or player-opponent == 2:
#     print("lose")
# elif player

