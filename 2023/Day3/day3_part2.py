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
                prevDigits.update({range(matchSymbol.start(), matchSymbol.end()): int(matchSymbol.group())})

        if x != len(keys)-1:
            for matchSymbol in re.finditer('\d+', keys[x+1]):
                nextDigits.update({range(matchSymbol.start(), matchSymbol.end()): int(matchSymbol.group())})
        
        for matchSymbol in re.finditer('\d+', keys[x]):
            currentDigits.update({range(matchSymbol.start(), matchSymbol.end()): int(matchSymbol.group())})


        # Check for asterisks in current line
        for match in re.finditer('[*]', value):    
            asteriskPositions = list(range(match.start()-1, match.end()+1))
            factor = 1
            counter = 0

            # Check for any matches with symbols
            if iterateDigitPositions(asteriskPositions, list(prevDigits.keys())):
                firstRange = iterateDigitPositions(asteriskPositions, list(prevDigits.keys()))
                factor *= (prevDigits.get(firstRange))
                counter += 1
                del prevDigits[firstRange]

                if iterateDigitPositions(asteriskPositions, list(prevDigits.keys())):
                    factor *= (prevDigits.get(iterateDigitPositions(asteriskPositions, list(prevDigits.keys()))))
                    counter += 1

            if iterateDigitPositions(asteriskPositions, list(nextDigits.keys())):
                firstRange = iterateDigitPositions(asteriskPositions, list(nextDigits.keys()))
                factor *= (nextDigits.get(firstRange))
                counter += 1
                del nextDigits[firstRange]

                if iterateDigitPositions(asteriskPositions, list(nextDigits.keys())):
                    factor *= (nextDigits.get(iterateDigitPositions(asteriskPositions, list(nextDigits.keys()))))
                    counter += 1

            if iterateDigitPositions(asteriskPositions, list(currentDigits.keys())):
                leftRange = iterateDigitPositions(asteriskPositions, list(currentDigits.keys()))
                factor *= (currentDigits.get(leftRange))
                counter += 1
                del currentDigits[leftRange]

                if iterateDigitPositions(asteriskPositions, list(currentDigits.keys())):
                    factor *= (currentDigits.get(iterateDigitPositions(asteriskPositions, list(currentDigits.keys()))))
                    counter += 1

            if counter == 2:
                gamesTotal += factor

    print('The answer is', gamesTotal)     


def iterateDigitPositions(symbolList, digitList):
    for range in digitList:
        for x in range:
            if any(i in symbolList for i in range):
                return range
        
               
# Test Case
# getSum("""100.100..
# ...*.....
# ..100-100
# ......-..
# 100......
# .....*100
# ..100....
# ......100
# .....*100""")

getSum(aocd.get_data(day=3, year=2023))