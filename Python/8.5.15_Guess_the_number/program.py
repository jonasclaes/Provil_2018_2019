# Jonas Claes - 10/05/2019 13:27
import random

# Choose a random number between 0 and 100.
chosenNumber = random.randint(0, 100)

# Keep track of the amount of tries.
count = 0

while count != 10:
    count += 1
    userNumber = int(input("Kies een nummer tussen 0 en 100 [Beurt %i]: " % count))
    if userNumber > chosenNumber:
        print("Fout! Dit nummer is te groot, probeer opnieuw.")
    if userNumber < chosenNumber:
        print("Fout! Dit nummer is te klein, probeer opnieuw.")
    if userNumber == chosenNumber:
        print("Juist!!! U heeft het nummer correct geraden!")
        input("Druk op 'ENTER' om het programma te sluiten...")
        exit(1)

print("Game over!")
input("Druk op 'ENTER' om het programma te sluiten...")