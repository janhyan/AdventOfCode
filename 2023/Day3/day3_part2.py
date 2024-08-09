# DAY 3 #

import aocd
import re

def getSum(input):
    gamesTotal = 0
    keys = input.splitlines()

    for x, value in enumerate(keys):
        prevDigits = {}
        nextDigits = {}
        currentDigits= {}

        # Check for any digits before and after the current line
        if x != 0:
            for matchSymbol in re.finditer('\d+', keys[x-1]):
                prevDigits.update({matchSymbol.span(): int(matchSymbol.group())})

        if x != len(keys)-1:
            for matchSymbol in re.finditer('\d+', keys[x+1]):
                nextDigits.update({matchSymbol.span(): int(matchSymbol.group())})
        
        for matchSymbol in re.finditer('\d+', keys[x]):
            currentDigits.update({matchSymbol.span(): int(matchSymbol.group())})


        # Check for asterisks in current line
        for match in re.finditer('[*]', value):    

            # Check for any matches with symbols
            print(prevDigits.keys())
            if any(i in prevDigits.keys() for i in range(match.start()-1, match.end()+1)):
                gamesTotal += prevDigits[i]

            if any(i in nextDigits.keys() for i in range(match.start()-1, match.end()+1)):
                gamesTotal += int(match.group())

            if any(i in currentDigits.keys() for i in range(match.start()-1, match.end()+1)):
                gamesTotal += int(match.group())   

    print('The answer is', gamesTotal)        
            
               
# Test Case
getSum("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""")

# getSum(aocd.get_data(day=3, year=2023))