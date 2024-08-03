# DAY 2 #

import aocd
import re

# print(aocd.get_data(day=2, year=2023))

def getTotalForGame():
    gameTotals = ['1 red']
    for x in gameTotals:
        gameTotals = re.findall(r"\d(?=red)", '1 red')

    print(gameTotals)

getTotalForGame()