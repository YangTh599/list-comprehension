# Using list comprehension to rewrite uppercase student names in lowercase
# but only when the student name is made up of four or more characters
students = ['MARK', 'JACKSON', 'ELENA', 'PHILLIP', 'KELSEY', 'LEE', 'ANGIE']
lowercase_students = [student.lower( ) for student in students if len(student) >= 4]
print(lowercase_students)