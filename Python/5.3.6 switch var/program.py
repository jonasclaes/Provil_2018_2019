print("------------------------------------")
print("********* Woorden switchen *********")
print("------------------------------------")

# Input temperatuur in Celsius
woord1 = input("Woord 1: ")
woord2 = input("Woord 2: ")

# Output
print()
print("Woord 1: " + woord1.upper())
print("Woord 2: " + woord2.upper())
print()

# Switchen van woorden
woord1, woord2 = woord2, woord1

# Output
print()
print("Woord 1: " + woord1.upper())
print("Woord 2: " + woord2.upper())
print()

# Workaround wachten tot enter
input("Druk op Enter om door te gaan...")
