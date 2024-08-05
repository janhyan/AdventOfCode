# DAY 2 #

import aocd
import re

# Create function to get totals and adds to list

def getTotalForGame(input):
    gamesTotal = 0

    # Loops through each line for red, blue, and green
    for x, value in enumerate(input.splitlines()):
        red = max(map(int, re.findall(r"(\d|\d{2})(?= red)", value)))
        blue = max(map(int, re.findall(r"(\d|\d{2})(?= blue)", value)))
        green = max(map(int, re.findall(r"(\d|\d{2})(?= green)", value)))
        
        gamesTotal += red * blue * green

    print("The answer is", gamesTotal)
    

getTotalForGame(aocd.get_data(day=2, year=2023))


