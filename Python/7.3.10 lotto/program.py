# Jonas Claes - 05/05/2019 11:27
import random

# Create list with availble ball numbers
availableNumbers = list(range(1, 46))
chosenNumbers = []

# Choose 7 numbers
for i in range(7):
    chosenNumbers.append(random.choice(availableNumbers))

# Print the first 6 numbers
for number in range(6):
    print("Ball #%i is %i." % (number + 1, chosenNumbers[number]))

# Print the bonus number
print("Bonus ball is %i" % chosenNumbers[6])

input("Press ENTER to end the program...")
