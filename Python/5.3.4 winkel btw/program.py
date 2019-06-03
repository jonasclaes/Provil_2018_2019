print("------------------------------------")
print("************ Winkel BTW ************")
print("------------------------------------")

# Input prijs incl. btw
floatOriginalPrice = float(input("Prijs inclusief BTW (€): "))
floatBtwPercentage = float(input("BTW (%): "))

# Berekeningen
# Berekenen van juiste btw (btw / 100 + 1)
# Ex: 21% -> (21 / 100 + 1) = 1.21
floatBtwPercentage = floatBtwPercentage / 100 + 1

# Output
print()
print("Prijs exclusief BTW: " + str(floatOriginalPrice / floatBtwPercentage))
print()

# Workaround wachten tot enter
input("Druk op Enter om door te gaan...")
