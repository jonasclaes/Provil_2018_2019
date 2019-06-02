# Jonas Claes - 02/06/2019 12:19

# Store exam results.
examResults = []

# Get all the results.
for i in range(0, 5):
        examResults.append(int(input("Exam %i result? " % (i + 1))))

# Sort exam results from low to high.
examResults.sort()

# Check if first two elements are below 50.
if (examResults[0] < 50 and examResults[1] < 50):
        print("You failed because you have more than 1 failed test.")
        input("Press 'ENTER' to exit...")
        exit(1)

# Calculate total.
total = 0
for result in examResults:
        total += result

# Calculate average.
average = total / 5

# Check if average is less than 50.
if (average < 50):
        print("You failed because your average was %i" % int(average))
        input("Press 'ENTER' to exit...")
        exit(1)

print("You passed.")
input("Press 'ENTER' to exit...")