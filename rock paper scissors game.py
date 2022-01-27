import random

rock = 1
paper = 2
scissors = 3

names = {rock: 'Rock', paper: 'Paper', scissors: 'Scissors'}
winning_items = {rock: scissors, paper: rock, scissors: paper}
winning_actions = { rock: 'crushes', paper: 'covers', scissors: 'cuts'}
pictures = {rock:"   0011100 \n  0       0 \n 0      1  0 \n 0      0   0 \n0    1 0      0\n0     0       0\n00   0      00 \n 000111011010 ", paper:"111111111111111 \n1             1 \n1 0           1 \n1             1 \n1             1 \n1 0           1 \n1             1 \n1             1 \n1 0           1 \n111111111111111", scissors:"           11 \n          11 \n         11 \n 000    11 \n0   01111111111 \n0   0111111111 \n 000  11 \n     11 \n 00011 \n0   0 \n0   0 \n 000 " }


def play_game():
        get_input()
        get_winner()
        stop_game()
            

    
#Welcome Player
def intro():
    print('Welcome to Rock, Paper, Scissors game! ')
    

def get_input():
    global player_input
    global computer_input
    player_input = (input('Choose 1 for Rock, 2 for Paper, or 3 for Scissors! ')) #Get player input as int
    if player_input == '1' or player_input =='2' or player_input == '3':
        player_input = int(player_input)
        print()
        computer_input = random.randrange(1,4)  #Randomize Computer input
    else: 
        print('\nInvalid input please only use 1 for Rock, 2 for Paper, or 3 for Scissors. ')
        get_input()

def get_winner(): #Main Loop Function
        if computer_input == player_input:  #Test Computer input against player input
            print('You both chose {},\n'.format(names[player_input])) #Display tie!
            print("{} \n\nYou Both Chose!\n\n{}\n\nIT'S A TIE!".format(pictures[player_input], pictures[computer_input]))
            
        elif winning_items[player_input] == computer_input: #Display user as winner!
            print("Your {} {} the computer's {}!\n".format(names[player_input], winning_actions[player_input], names[computer_input]))
            print('{} \n\nBEATS!\n\n{}\n\nYOU WIN!!!'.format(pictures[player_input], pictures[computer_input]))
            
        else: #Display Computer as winner :(
            print("The computer's {0} {1} your {2}!\n".format(names[computer_input], winning_actions[computer_input], names[player_input]))
            print('{} \n\nBEATS\n\n{}\n\nYOU LOSE...'.format(pictures[computer_input], pictures[player_input]))

def stop_game():
        user_interrupt = str(input('Would you like to play again? Y to play again N to exit game. '))  #Ask player to play again
        
        if user_interrupt == "N" or user_interrupt == "n":
            print('Thanks for playing Rock, Paper, Scissors game!') #Stop game for player
        
        elif user_interrupt =="Y" or user_interrupt == "y":
            play_game()
            
        else:
            print('\nInvalid input please type either Y to continue or N to stop the game.')
            stop_game()
    
           
intro()      
play_game()
