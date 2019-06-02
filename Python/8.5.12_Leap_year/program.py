# Jonas Claes - 02/06/2019 13:18

# Get year.
year = int(input("Year? "))

if (not year % 4 and year % 100):
        print("%i is a leap-year." % year)
        input("Press 'ENTER' to exit...")
        exit(1)

if (not year % 400):
        print("%i is a leap-year." % year)
        input("Press 'ENTER' to exit...")
        exit(1)

print("%i is not a leap-year." % year)
input("Press 'ENTER' to exit...")