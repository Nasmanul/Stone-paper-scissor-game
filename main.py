from random import randint
import time
print('Stone paper scissor')
feeling_brave = True
score = 0
while feeling_brave:
    game = randint(1, 3)
    print('Select any number from Stone paper or scissor')
    print('1- Stone\n2- Paper\n3- Scissor')
   # print('Ghost door')
    #print(ghost_door)
    door = input('1, 2, or 3\n')
    door=int(door)
    if(door==1):
        print('Your answer is Stone')
    elif(door==2):
        print('Your answer is Paper')
    elif(door==3):
        print('Your answer is Scissor')
    if(game==1):
        print('computer answer is Stone')
    elif(game==2):
        print('computer answer is Paper')
    elif(game==3):
        print('computer answer is Scissor')
    #print('Computer answer is', game)
    print("\n")
    if (door == game == 1 or door == game == 2 or door == game == 3):
        print('Draw')
        print('Game Over!')
        time.sleep(2)
        feeling_brave = False
    elif(door == 1 and game == 2):
        print("You failed, computer won")
        time.sleep(2)
        feeling_brave = False
    elif(door == 1 and game == 3):
        print('You won, Congratulations!!')
        time.sleep(2)
        feeling_brave = False
    elif(door == 2 and game == 1):
        print('You won, Congratulations!!')
        time.sleep(2)
        feeling_brave = False
    elif(door == 2 and game == 3):
        print("You failed, computer won")
        time.sleep(2)
        feeling_brave = False
    elif(door == 3 and game == 1):
        print("You failed, computer won")
        time.sleep(2)
        feeling_brave = False
    elif(door == 3 and game == 2):
        print('You won, Congratulations!!')
        time.sleep(2)
        feeling_brave = False

    else:
        print('Enter valid number!!')
        time.sleep(2)
        feeling_brave = False
        
#if feeling_brave == false:
print('Thankyou')


