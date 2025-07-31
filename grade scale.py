mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))
mark4 = int(input("Enter marks for subject 4: "))
mark5 = int(input("Enter marks for subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

if average >= 95:
    grade = "A"
elif average >= 92:
    grade = "B"
elif average >= 91:
    grade = "C"
elif average >= 88:
    grade = "D"
elif average >= 85:
    grade = "E"
else:
    grade = "F"

print(f"The grade of the student is: {grade}")
