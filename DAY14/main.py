import random
from game_data import data
from art import logo, vs

print(logo)

def display(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check(user_choice, a_followers, b_followers):
    if a_followers > b_followers:
        correct_answer = "a"
    else:
        correct_answer = "b"
    return user_choice == correct_answer

score = 0
game_over = False

account_A = random.choice(data)
account_B = random.choice(data)

# ensure A and B are not the same
while account_A == account_B:
    account_B = random.choice(data)

while not game_over:
    print(f"\nCompare A: {display(account_A)}")
    print(vs)
    print(f"Against B: {display(account_B)}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_A["follower_count"]
    b_followers = account_B["follower_count"]

    result = check(user_choice, a_followers, b_followers)

    if result:
        score += 1
        print(f"You're right! Current score: {score}")

        # B becomes new A
        account_A = account_B

        # pick new B
        account_B = random.choice(data)
        while account_A == account_B:
            account_B = random.choice(data)

    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
