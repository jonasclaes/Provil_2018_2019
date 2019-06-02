# Jonas Claes - 02/06/2019 12:34

def getPrice(price, people, discount):
        return (people * price) * (1 - (discount / 100))

# Get amount of people.
amount = int(input("Amount of people? "))

# Check if amount is bigger than 10.
if (amount >= 10):
        # Give 100% discount.
        print("U betaalt %.2f" % getPrice(10, amount, 100))
        input("Press 'ENTER' to exit...")
        exit(1)

# Check if amount is bigger or equal to 6.
if (amount >= 6):
        # Give 40% discount.
        print("U betaalt %.2f" % getPrice(10, amount, 40))
        input("Press 'ENTER' to exit...")
        exit(1)

# Check if amount is bigger or equal to 4.
if (amount >= 4):
        # Give 20% discount.
        print("U betaalt %.2f" % getPrice(10, amount, 20))
        input("Press 'ENTER' to exit...")
        exit(1)

# Check if amount is equal to 3.
if (amount == 3):
        # Give 10% discount.
        print("U betaalt %.2f" % getPrice(10, amount, 10))
        input("Press 'ENTER' to exit...")
        exit(1)

print("U betaalt %.2f" % getPrice(10, amount, 0))
input("Press 'ENTER' to exit...")