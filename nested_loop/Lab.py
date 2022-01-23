student_name = input()
current_year = 1
bad_grades = 0
year_grades = 0
total_grade = 0

while current_year <= 12:
    year_grades = float(input())
    if year_grades < 4:
        bad_grades = bad_grades + 1
        if bad_grades == 2:
            break
    total_grade = total_grade + year_grades
    current_year = current_year + 1
if current_year == 13:
    total_grade = total_grade / 12
    print(f'{student_name} graduated. Average grade: {total_grade:.2f}')
else:
    print(f'{student_name} has been excluded at {current_year - 1} grade')