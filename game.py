import random

OPERATORS = ["rock", "paper", "scissors"]

def is_a_win(user_choice, bot_choice):
    return (user_choice == "rock" and bot_choice == "scissors" or
            user_choice == "scissors" and bot_choice == "paper" or
            user_choice == "paper" and bot_choice == "rock")

win_streak = 0
lose_streak = 0
tie_streak = 0

while(True):

    bot_choice = random.choice(OPERATORS)
    user_choice = input("\nType  option: ").lower()

    if(user_choice == "quit"):
        print(f'You have a rating of w:{win_streak}/ t:{tie_streak}/ l:{lose_streak}')
        quit()

    if user_choice not in OPERATORS:
        print(f'Please make a choice from {OPERATORS}')
        continue
        
    print(f'Bot choice is {bot_choice}')

    if is_a_win(user_choice,bot_choice):
        print("Congratulations! You won~ :)")
        win_streak += 1
        continue
    elif is_a_win(bot_choice, user_choice):
        print("Try better next time! You lose :(")
        lose_streak += 1
        continue
    else:
        print("Its a " + random.choice(["draw", "tie"]) + ". Try better next time. :|")
        tie_streak += 1
        continue