
puzzleArray = []
puzzleKey = input("Enter puzzle keys: \n")

while puzzleKey != 'exit':
    puzzleArray.append(puzzleKey)
    puzzleKey = input()

puzzleCode = []

for x in range(len(puzzleArray)):
    firstInt = '0'
    secondInt = '0'

    for count, character in enumerate(puzzleArray[x]):
        intCheck = False
        if character.isdigit() == True and intCheck == False:
            firstInt = character
            intCheck = True
        elif character.isdigit() == True:
            secondInt = character

    puzzleCode.append(int(firstInt + secondInt))


for x in range(len(puzzleCode)):
    print(puzzleCode[x])