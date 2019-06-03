print("------------------------------------")
print("********** Tafels oefenen **********")
print("------------------------------------")

# Input
intTafel = int(input("Tafel van: "))

# Output
for i in range(1, 11):
    print("%d x %d = %d" % (i, intTafel, i * intTafel))

# End
input("Druk op Enter om verder te gaan...")
