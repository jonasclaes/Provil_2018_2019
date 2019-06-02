# Jonas Claes - 02/06/2019 12:13

# Create blacklist.
blacklist = ["jonas@alterit.be"]

# Get user email address.
mail = input("What is your email address? ")

# Loop over each email address.
for item in blacklist:

    # Check if mail is on blacklist.
    if mail == item:
        print("Your email has been blacklisted.")
        input("Press 'ENTER' to exit...")
        exit(0)

# Email has not been blacklisted.
print("Your email address has not been blacklisted.")
input("Press 'ENTER' to exit...")