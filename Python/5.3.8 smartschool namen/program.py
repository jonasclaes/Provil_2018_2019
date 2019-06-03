print("-----------------------------------")
print("******** Smartschool namen ********")
print("-----------------------------------")

# Input
strFullname = input("Volledige naam: ")

arrNames = strFullname.split(" ", 1)

# Output
print()
print("Smartschool naam: " + arrNames[1][0:3].upper() + arrNames[0][0:2].upper())
print()

# End
input("Druk op Enter om door te gaan...")