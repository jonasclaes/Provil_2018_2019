# Leerlingen en volgnummers

print("-- Leerlingen volgnummers --")

# Initialize array of student names
students = []

# Amount of students
amountOfStudents = int(input("Aantal leerlingen? "))

# Get each students name
for i in range(1, amountOfStudents + 1):
    name = input("Naam van student %i? " % i)
    students.append(name)

# Sort students into different array
sortedStudents = sorted(students)

# Print blank line for visual purposes
print("")

for student in students:
    print("Student \"%s\" heeft klasnummer %i." % (student, sortedStudents.index(student) + 1))
