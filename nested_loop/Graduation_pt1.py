name = input()
grades_counter = 1
current_grade = 0
total_grades = 0

while grades_counter <= 12:
    current_grade = float(input())
    if current_grade >= 4:
        grades_counter = grades_counter + 1
        total_grades = total_grades + current_grade

average_grade = total_grades / 12
print(f'{name} graduated. Average grade: {average_grade:.2f}')