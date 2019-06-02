# Jonas Claes - 02/06/2019 13:28
import random

results = []

# Get amount of simulations.
endRange = int(input("How many simulations should be run? "))

# Run simulations.
for i in range(1, endRange):
    results.append(random.randint(1, 6))

# Return counts.
print("1 has been thrown %i times which is %.2f percent" % (results.count(1), (results.count(1) * 100) / endRange))
print("2 has been thrown %i times which is %.2f percent" % (results.count(2), (results.count(2) * 100) / endRange))
print("3 has been thrown %i times which is %.2f percent" % (results.count(3), (results.count(3) * 100) / endRange))
print("4 has been thrown %i times which is %.2f percent" % (results.count(4), (results.count(4) * 100) / endRange))
print("5 has been thrown %i times which is %.2f percent" % (results.count(5), (results.count(5) * 100) / endRange))
print("6 has been thrown %i times which is %.2f percent" % (results.count(6), (results.count(6) * 100) / endRange))

input("Press 'ENTER' to exit...")