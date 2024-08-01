# PART TWO #

import re

# Declare initial input for while loop to check
puzzleArray = []
puzzleKey = input("Enter puzzle keys: \n")              

# Allows infinite input until exit is given
while puzzleKey != 'exit':
    puzzleArray.append(puzzleKey)
    puzzleKey = input()

puzzleCode = []

# Loops through each key and takes the first and last integer
for x in range(len(puzzleArray)):
    # patterns = ['one', 'two', 'three',
    #             'four', 'five', 'six',
    #             'seven', 'eight', 'nine']
    keys = re.findall(r"\Bone\B|\Btwo\B|\Bthree\B|\Bfour\B|\Bfive\B|\Bsix\B|\Bseven\B|\Beight\B|\Bnine\B|", puzzleArray[x])
    print(keys[x])

