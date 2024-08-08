# DAY 3 #

import aocd
import re

def getSum(input):
    gamesTotal = 0
    keys = input.splitlines()

    for x, value in enumerate(keys):
        prevSymbols = []
        nextSymbols = []
        currentSymbols = []

        # Check for any symbols before and after the current line
        if x != 0:
            for matchSymbol in re.finditer("[^(?!0-9|.)]", keys[x-1]):
                prevSymbols.append(matchSymbol.start())

        if x != len(keys)-1:
            for matchSymbol in re.finditer("[^(?!0-9|.)]", keys[x+1]):
                nextSymbols.append(matchSymbol.start())
        
        for matchSymbol in re.finditer("[^(?!0-9|.)]", keys[x]):
            currentSymbols.append(matchSymbol.start())


        # Check for digits in current line
        for match in re.finditer('\d+', value):    

            # Check for any matches with symbols
            if any(i in prevSymbols for i in range(match.start()-1, match.end()+1)):
                gamesTotal += int(match.group())

            if any(i in nextSymbols for i in range(match.start()-1, match.end()+1)):
                gamesTotal += int(match.group())

            if any(i in currentSymbols for i in range(match.start()-1, match.end()+1)):
                gamesTotal += int(match.group())   

    print('The answer is', gamesTotal)        
            
               
# Test Case
# getSum("""467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""")

getSum(aocd.get_data(day=3, year=2023))