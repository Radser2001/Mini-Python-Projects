print('''
            #################################
                CHOOSE YOUR OWN ADVENTURE
            #################################
''')

name = input("Type your name: ")
print("\n-------WELCOME TO THIS ADVENTURE", name.upper() , "! -------\n")
print("LET'S GO!!!!\n\n")

print("------------------------------------------------------------------------------------------------------------------------------------")
answer = input("-You are on a dirt road, it has come to an end and you can go left to or right. Which way would you like to go ? ").lower()


if answer == "left":
    answer = input("-You come to a river, you can walk around it or swim accross. Type 'walk' to walk around and 'swim' to swim accross: ").lower()

    if answer == "swim":
        print("-You swam accross and were eaten by an alligator.")
    
    elif answer == "walk":
        print("-You walked for mant miles, ran out of water and you lost the game.")
    
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("-You came to a bridge, it looks wobbly, do you want to cross ot or head back (cross/back)? ").lower()
    
    if answer == "back":
        print("-You go back and lose.")
    
    elif answer == "cross":
        answer = input("-You cross the bridge and met a stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("-You talk to the stranger and they give you god. You WIN!")
        elif answer == "no":
            print("-You ignore the stranger and they are offended and you LOSE!")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")


else:
    print("Not a valid option. You lose.")

print("\n\n-------THANK YOU FOR TRYING", name.lower(), " -------")

print("------------------------------------------------------------------------------------------------------------------------------------")
