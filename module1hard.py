grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

grades_1 = grades[0]
grades_2 = grades[1]
grades_3 = grades[2]
grades_4 = grades[3]
grades_5 = grades[4]

grades_1_sr = sum(grades_1) / len(grades_1)
grades_2_sr = sum(grades_2) / len(grades_2)
grades_3_sr = sum(grades_3) / len(grades_3)
grades_4_sr = sum(grades_4) / len(grades_4)
grades_5_sr = sum(grades_5) / len(grades_5)

grades_sr = [grades_1_sr, grades_2_sr, grades_3_sr, grades_4_sr, grades_5_sr]

students_grades_sr = dict(zip(students, grades_sr))

print(students_grades_sr)
