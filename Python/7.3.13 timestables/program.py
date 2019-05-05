# Jonas Claes - 05/05/2019 11:30
import random

# Ask for the biggest number
biggestNumber = int(input("What is the biggest number? "))

maxExercises = biggestNumber**2

# Ask for the amount of exercises
exercises = int(input("How many exercises do you want to generate (max %i)? " % maxExercises))

# Check if the amount of exercises doesnt exceed the maximum number of combinations
while exercises > maxExercises:
    exercises = int(input("How many exercises do you want to generate (max %i)? " % maxExercises))

# Create a list with available numbers
availableNumbers = list(range(1, biggestNumber + 1))

# Left and right hand side for picked numbers
leftSide = []
rightSide = []

for exerciseNumber in range(exercises):
    # Pick left side
    leftSideTemp = random.choice(availableNumbers)

    # Pick right side
    rightSideTemp = random.choice(availableNumbers)

    # Check if exercise has already been formed before
    equality = True
    while equality:
        equality = False

        # Test every possible combination
        for testNumber in range(len(leftSide)):
            while leftSide[testNumber] == leftSideTemp and rightSide[testNumber] == rightSideTemp:
                # Pick left side again
                leftSideTemp = random.choice(availableNumbers)

                # Pick right side again
                rightSideTemp = random.choice(availableNumbers)

                # Restart with new numbers
                equality = True

    # Add left and right side to the corresponding arrays
    leftSide.append(leftSideTemp)
    rightSide.append(rightSideTemp)

    # Print out times table
    print("- Exercise %i:\t\t%i x %i = ..." % (exerciseNumber + 1, leftSide[exerciseNumber], rightSide[exerciseNumber]))

input("\nPress ENTER to see the results...")

for exerciseNumber in range(exercises):
    # Print out times table with results
    print("- Exercise %i:\t\t%i x %i = %i" % (exerciseNumber + 1, leftSide[exerciseNumber], rightSide[exerciseNumber], leftSide[exerciseNumber] * rightSide[exerciseNumber]))

input("Press ENTER to end the program...")
