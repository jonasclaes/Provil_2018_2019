# Jonas Claes 23-04-2019 14:04
import random, string

choices = string.printable[0:94]
password = ""

for i in range(1, 16):
    password += random.choice(choices)

print("Your generated password is:")
print(password)
input("Press enter to exit the program...")