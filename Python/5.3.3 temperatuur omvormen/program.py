print("-----------------------------------")
print("** Celsius - Kelvin - Fahrenheit **")
print("-----------------------------------")

# Input temperatuur in Celsius
floatCelsius = float(input("Temperatuur in graden Celsius: "))

# Output
print()
print("Temperatuur in graden Celsius: " + str(round((floatCelsius * 1000)) / 1000))
print("Temperatuur in graden Kelvin: " + str(round((floatCelsius + 273.5) * 1000) / 1000))
print("Temperatuur in graden Fahrenheit: " + str(round((floatCelsius * 1.8 + 32) * 1000) / 1000))
print()

# Workaround wachten tot enter
input("Druk op Enter om door te gaan...")
