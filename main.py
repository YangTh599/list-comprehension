# Thayer Yang
# 12 NOV 2024
# List Comprehension

#Filtered Lowercase Names

students = ["THAYER", "APOLLOS", "ISAAC", "JOSH", "LUCAS"]

new_students = []
for student in students:
    if len(student) >= 4:
        new_students.append(student.lower())

print(new_students)

#Inches to Centimeters

inches = [14, 20, 36, 40, 52, 60, 72, 92]

centimeters = []

for measurement in inches:
    converted = measurement * 2.54
    centimeters.append(converted)

print(f'Inches: {inches}')
print(f'Centimeters: {centimeters}')

# Filtered Last Names

last_names = ['Brimley', "Baran", "Ovaitt", "Friday",'Tower', 'Beckwitch', "Willis"]

b_last_names = []
for name in last_names:
    if name.lower()[0:1] == 'b':
        b_last_names.append(name)

print(f"All Last Names: {last_names}")
print(f'B Last Names: {b_last_names}')