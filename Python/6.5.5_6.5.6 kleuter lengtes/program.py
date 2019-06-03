# Check if a number is odd or not
def isOdd(number):
    return number & 1


# Get the average of an array
def averageOfArray(arr):
    return sum(arr)/len(arr)


# Here we print our heading
def print_heading():
    print("---------------------------------")
    print("---- Lengtes van de kinderen ----")
    print("---------------------------------\r\n")


# Print our formatted output with a specific array
def print_output(arr):
    print("De grootse leerling is %0.2fm groot." % max(arr))
    print("De kleinste leerling is %0.2fm groot." % min(arr))
    print("Alle leerlingen op elkaar gestapeld zijn samen %0.2fm groot." % sum(arr))

    # Print average
    print("De gemiddelde leerling is %0.2fm groot." % averageOfArray(arr))

    # Check if array is odd or even
    if isOdd(len(arr)):
        # Array is odd so we can get the median pretty easy
        print("Het mediaan is %0.2fm groot." % arr[len(arr) // 2])
    else:
        # Array is even
        length = len(arr)
        firstmiddle = arr[length // 2 - 1]
        secondmiddle = arr[length // 2]
        median = (firstmiddle + secondmiddle) / 2
        print("Het mediaan is %0.2fm groot." % median)


lengtes = [1.05, 1.10, 1.3, 1.03, 1.04, 0.95, 0.93]

print_heading()
print_output(lengtes)

lengtes.append(float(input("\r\nLengte van de nieuwe leerling? ")))

print_heading()
print_output(lengtes)

input("\r\nPress enter to exit...")