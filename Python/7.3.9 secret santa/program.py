# Jonas Claes - 05/05/2019 10:35
import random, os

friends = []
friendsRemaining = []
flagAdd = True

# Get name
friends.append(str(input("Naam van persoon? ")))

# Add friends to list
while (flagAdd):
    # Get name
    friends.append(str(input("Naam van persoon? ")))

    # Check if they want to add another friend to the list.
    if input("Nog een persoon toevoegen [J/n]: ").lower() == "n":
        flagAdd = False

friendsRemaining = friends.copy()

for i in range(len(friends)):
    # Print the available choosers.
    for i in range(len(friends)):
        print("%i. %s" % (i + 1, friends[i]))

    # Which person is choosing?
    num = int(input("Wie bent u (nummer)? ")) - 1
    while num + 1 > len(friends):
        num = int(input("Wie bent u (nummer)? ")) - 1

    # Choose a random name
    name = random.choice(friendsRemaining)

    # While the name is equal to the choosers name, try again.
    while name == friends[num]:
        name = random.choice(friendsRemaining)

    # Remove person from availble choosers.
    friends.pop(num)

    # Remove the chosen name from the remaining list.
    friendsRemaining.remove(name)

    # Print who needs to buy the gift.
    print("U moet een cadeau kopen voor %s." % name)

    # Clear the screen to let the next person choose.
    input("Press ENTER to let the next person choose.")
    os.system('clear' if os.name == 'posix' else 'cls')

input("Press ENTER to end the program...")
