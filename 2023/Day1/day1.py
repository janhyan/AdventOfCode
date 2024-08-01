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
    firstInt = None
    secondInt = None
    intCheck = False

    for count, character in enumerate(puzzleArray[x]):     
        if character.isdigit() == True and intCheck == False:
            firstInt = character
            intCheck = True
        elif character.isdigit() == True:
            secondInt = character
    
    if secondInt == None:
        secondInt = firstInt

    puzzleCode.append(int(firstInt + secondInt))

print("{}{}".format("The answer is ", sum(puzzleCode)))

