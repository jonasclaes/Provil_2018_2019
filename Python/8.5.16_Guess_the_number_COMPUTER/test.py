chosenNumber = int(input("Number? "))

rangeNumber = 100
previousNumber = 0

count = 0

while count != 10:
    count += 1
    rangeNumber = (100 - previousNumber) // 2
    previousNumber = rangeNumber + previousNumber
    print("rangeNumber: %i; previousNumber: %i; try: %i" % (rangeNumber, previousNumber, count))
    if previousNumber == chosenNumber:
        exit()
