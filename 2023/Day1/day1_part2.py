# PART TWO #

import re

# Declare initial input for while loop to check
puzzleArray = []
puzzleKey = input("Enter puzzle keys: \n")              

# Allows infinite input until exit is given
while puzzleKey != 'exit':
    puzzleArray.append(puzzleKey)
    puzzleKey = input()

# Convert number words to integer

def word2int(word):
    ones = {
        "one": '1', "two": '2', "three": '3',
        "four": '4', "five": '5', "six": '6',
        "seven": '7', "eight": '8', "nine": '9'
    }

    if word in ones:
        return ones[word]
    else:
        return word

puzzleCode = []

# Loops through each key and takes the first and last integer
for x in range(len(puzzleArray)):
    keys = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", puzzleArray[x])

    puzzleCode.append(int(word2int(keys[0]) + word2int(keys[len(keys)-1])))
  
print("{}{}".format("The answer is ", sum(puzzleCode)))

