students = [("Saad", 29), ("Rahil", 99), ("Akki", 69)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print(sorted_students)