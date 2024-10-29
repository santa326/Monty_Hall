#This is a simulation for Monty Hall Problem


#https://www.youtube.com/watch?v=4Lb-6rxZxx0
import random

# n is number of rounds played. ~Simulations
n = 10000

# There are 3 Combos of Doors
Combos = [["Car","Goat","Goat"],["Goat","Car","Goat"],["Goat","Goat","Car"]]

# A Player can any of the 3 doors. I know they are 1,2,3  
Choices = [0,1,2]



#We will keep the scores from each game . For any game the player win by either staying with their choice or switching to the other available door
Stay_score = 0
Switch_Score = 0

#While loop to run n times
#Picks a combo of Car/Goat/Goat randomly , Picks a door randomly ,As a host we expose the Goat in one of the other rooms
run = 0
while run != n:
    Round = random.choice(Combos)
    run = run + 1
    #Players makes a choice
    first_choice = random.choice(Choices)
    
    rest_doors = [0,1,2]
    #We get the remaining doors here
    rest_doors.remove(first_choice)
    
    #From the remaining doors , we show a random door if both contains goats
    #Else we show the one with a goat

    if Round[rest_doors[0]] == "Goat" and Round[rest_doors[1]] == "Goat":
        exposed = random.choice(rest_doors)
    else:
        if Round[rest_doors[0]] == "Car":
            exposed = rest_doors[1]
        else:
            exposed = rest_doors[0]

    #Record score, if the player picked car as first choice , we increment stay score , else we increment Switch score
    if Round[first_choice] == "Car":
        Stay_score = Stay_score + 1
    else:
        Switch_Score = Switch_Score + 1

  
print('Win Percentage when we stay :' + str((Stay_score/n)*100) + '%')
print('Win Percentage when we Switch :' + str((Switch_Score/n)*100)+ '%')
