# Get the starting fibonacci numbers
start1 = int(input("First fibonacci number: "))
start2 = int(input("Second fibonacci number: "))
# New line
print("")

fibonacci = [start1, start2]

for i in range(2, 102):
    current_fibonacci = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(current_fibonacci)

# Print all fibonacci numbers
for val in fibonacci:
    print(val)

input("\r\nPress enter to continue...")
