'''
Monty Hall Problem is a classic probability problem based on old TV show where you are given 3 doors behind which one door has car and other two doors have goat. 
Here is the outline or steps in the Monty Hall Problem:
    a) We choose a door (randomly)
    b) Host has to first show a door with a goat (except your chosen gate)
    c) Then we are given to stay with the original choice or switch the choice to the other door
    d) Based on winnings with switch and without switch is analyzed in the code for k iterations (ex. 100000)
'''

import random

def montyhall(doors,iterations):
    #define results 
    stay_chose = []
    switch_chose=[]

    for trails in iterations:
        #door assign to the car
        car_door = random.randint(1,3)
        #door first guess by the person
        first_guess = random.randint(1,3)
        #door which host opens up first i.e. not car door
        # ex. if person choose 1, then host can show 2 or 3 where goat is for sure
        door_goat = [door for door in doors if door != car_door]
        '''
        basically if the first guess is not the car door then host has only one option as among other 2 doors one will be car and one will be goat.
        However, if the first guess is the car then the host has 2 options where both of themn is the goat
        '''
        reveal_door_options = [door for door in door_goat if door!=first_guess]
        if len(reveal_door_options)==2:
            reveal_door = random.choices(reveal_door_options)
        else:
            reveal_door = reveal_door_options[0]
        '''
        Now host ask the person if he/she wants to switch door among two options left after showing the goat option.
        '''
        switch_door = [door for door in doors if door!= first_guess and door!=reveal_door][0] 
        '''
        now the person has the choice to switch between the door he chooses to be first guess and another door which is not a first guess and not a first reveal door
        '''
        if car_door == switch_door:
            switch_chose.append(1)
            stay_chose.append(0)
        else:
            switch_chose.append(0)
            stay_chose.append(1)
    
    switch_win = sum(switch_chose)/len(switch_chose)
    stay_win = sum(stay_chose)/len(stay_chose)
    
    return switch_win,stay_win

doors =[1,2,3]
#defining the number of trails to be done
iterations=range(100000)

print("The person probability in %s iterations to win after switching is %0.2f %% and to win staying with the original choice is %0.2f %%"%(len(iterations), montyhall(doors,iterations)[0]*100, montyhall(doors,iterations)[1]*100))

'''
The person probability in 100000 iterations to win after switching is 66.52 % and to win staying with the original choice is 33.40 %
'''



