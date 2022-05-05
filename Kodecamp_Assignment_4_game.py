# Creating a number guessing game
# import the random module and the randint function from it
from random import randint
#Setting the environment for the game
print('-----------------------------------------------------------------------------------------------------')
print()
print("---------    WELCOME TO NUMBER GUESSING GAME PORTAL!     -------")
print()
print('--------------------------------------------------------------------------------------------------------')
#receiving the preffered name for the player and generate a welcome message
player_name = input("\nEnter your game name:  ").title()
print('\n', player_name, 'you are welcome')
#set the computer choice to random using randint
comp_choice=randint(1, 10)
#receive input from the user to either play or close the game terminal and loop it
game_req = input("\nEnter 'Yes' to play or Enter 'No' to close the game terminal:   ").title()
for req in game_req:
    if game_req =='No':
        break
    elif game_req == 'Yes': 
        print("\n****0*1**3*4*5*------Game Loading------*2*3*4*5*6*****")
    else:
        print("Invalid Selection made: Reload the game")
        break
     #Assign the computer's choice to computer player named 'robot' 
    robot = comp_choice
    #generate choice of the robot for comparing purpose
    #print(f"robot selected: {robot}")
    #receive input of number from player between 1 and 10 or 0 to quit the game.
    player_guess = eval(input("Choose a number between 1 and 10 or 0 to quit the game:    "))
    if player_guess == 0:
        print("You quit the game")
        break
    elif player_guess == robot:
        print(f"{player_name} you guessed right, champ!!!")
        break
    elif player_guess > robot:
        print('Wrong choice, pick a number lesser than your previous choice:  ')
    #check if the player_guess is lesser than that of the robot
    elif player_guess < robot:
        print('Incorrect guess, choose a number greater that your previous choice:  ')
    else:
        if player == 3:
            print('time Over')
            print(f"robot selected: {robot}")        
print('Thank you')
print('Game Over')
