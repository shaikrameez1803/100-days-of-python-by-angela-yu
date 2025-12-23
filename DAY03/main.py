##TREASURE ISLAND PROJECT##
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('Which direction u wish to head towards? "Left" or "Right"').lower()
if choice1!="left":
    print("GAME OVER!!")
elif choice1=="left":
    choice2=input(('You are at stage 2\nWhat do you wish to?\n"Swim" or"Wait"')).lower()
    if choice2=="swim":
        print("GAME OVER!!")
    elif choice2=="wait":
        choice3=input(('You are at stage 3\n Whhic color door do you wish to choose?\n "Red" "Blue" "Yellow" '))
        if choice3=="yellow":
            print("YOU WINNN!!!!!!")
        else:
            print("GAME OVER!")
else:
    print("PLEASE SELECT A VALID CHOICE")