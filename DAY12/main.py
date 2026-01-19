##-------Number Guessing Game------##
import random

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


    #function to set difficulty
def set_difficulty():
    response=input("Choose a difficulty.Type 'easy' or 'hard'.").lower()
    if response=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#function to check user's guess against actual number
def check(user_guess,comp_num,turns):
    if user_guess>comp_num:
        print("Too High.")
        return turns-1
    elif user_guess<comp_num:
        print("Too Low")
        return  turns -1
    else:
        print(f"You got it!The answer was {comp_num} ")
        return turns

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    comp_num=random.randint(1,100)
    turns=set_difficulty()

    user_guess=0
    while user_guess!=comp_num and turns!=0:
            print(f"You have {turns} attempts remaining to guess the number")
            user_guess=int(input("Make a guess."))
            turns=check(user_guess,comp_num,turns)
            if user_guess==comp_num:
                return
            elif turns==0:
                print("You've run out of guesses. Refresh the page to run again.")

game()





#repeat the guessing functionality if they get it wrong
