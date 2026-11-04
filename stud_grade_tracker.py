print("=================================")
print("     STUD GRADE TRACKER")
print("=================================")

student_name = input("Enter student name: ")

number_of_subjects = int(input("Enter number of subjects: "))

total_weighted_grade = 0
total_units = 0

subjects = []
grades = []
units = []

for i in range(number_of_subjects):

    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")

    grade = float(input("Enter grade: "))

    unit = int(input("Enter units: "))

    subjects.append(subject)
    grades.append(grade)
    units.append(unit)

    total_weighted_grade += grade * unit
    total_units += unit
    gwa = total_weighted_grade / total_units
    if i == 0:
        highest_grade = grades[i]
        lowest_grade = grades[i]

    if grades[i] < highest_grade:
        highest_grade = grades[i]

    if grades[i] > lowest_grade:
        lowest_grade = grades[i]
        


print("\n=================================")
print("           GWA RESULT")
print("=================================")

print("Student:", student_name)
print()

print(f"{'Subject':<20} {'Grade':<10} {'Units':<10} {'Status':<10}")

for i in range(number_of_subjects):
    if grades[i] <= 3.00:
        status = "Passed"
    else:
        status = "Not Passed"

    grade_identifier = ""

    if grades[i] == highest_grade:
        grade_identifier = "(Highest Grade)"

    if grades[i] == lowest_grade:
        if grade_identifier != "":
            grade_identifier = "(Highest or Lowest Grade)"
        else:
            grade_identifier = "(Lowest Grade)"

    print(f"{subjects[i]:<20} {grades[i]:<10.2f} {units[i]:<10} {status:<8} {grade_identifier}")

print()
print(f"Your GWA: {gwa:.2f}")
print("Total Units:", total_units)
print("Subjects:", len(subjects))

if gwa <= 3.00:
    print("Overall Remarks: Passed")
else:
    print("Overall Remarks: Failed")

print("=================================")