import random

DICE_ONE = """
+-----------+
|           |
|     O     |
|           |
+-----------+
"""

DICE_TWO = """
+-----------+
|   O       |
|           |
|       O   |
+-----------+
"""

DICE_THREE = """
+-----------+
|   O       |
|     O     |
|       O   |
+-----------+
"""

DICE_FOUR = """
+-----------+
|   O   O   |
|           |
|   O   O   |
+-----------+
"""

DICE_FIVE = """
+-----------+
|   O   O   |
|     O     |
|   O   O   |
+-----------+
"""

DICE_SIX = """
+-----------+
|   O   O   |
|   O   O   |
|   O   O   |
+-----------+
"""

DICES = [DICE_ONE, DICE_TWO, DICE_THREE, DICE_FOUR, DICE_FIVE, DICE_SIX]

LOWEST = 6
HIGHEST = 1
SUM = 0

for throw in range(1, 11):
    rand = random.randint(1, 6)

    if rand > HIGHEST:
        HIGHEST = rand

    if rand < LOWEST:
        LOWEST = rand

    SUM += rand

    print("Throw %i results in a %i." % (throw, rand))
    print(DICES[rand - 1])
    input("Press 'enter' for the next throw...")

print("The highest throw was a %i, whilst the lowest throw was a %i, the total amount is equal to %i" % (HIGHEST, LOWEST, SUM))
input("Press 'enter' to exit...")