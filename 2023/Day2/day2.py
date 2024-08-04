# DAY 2 #

import aocd
import re

# Create function to get totals and adds to list

def getTotalForGame(input):
    gamesList = input.splitlines()
    gamesTotal = []

    # Loops through each line for red, blue, and green
    for x in range(len(gamesList)):
        red = re.findall(r"(\d|\d{2})(?= red)", gamesList[x])
        blue = re.findall(r"(\d|\d{2})(?= blue)", gamesList[x])
        green = re.findall(r"(\d|\d{2})(?= green)", gamesList[x])
        
        if all(int(i) <= 12 for i in red) and all(int(i) <= 14 for i in blue) and all(int(i) <= 13 for i in green): 
            gamesTotal.append(x + 1)

    print("The answer is", sum(gamesTotal))
    

getTotalForGame(aocd.get_data(day=2, year=2023))


