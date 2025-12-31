import pandas as pd

grades_df = pd.read_csv('data/grades.txt', sep=',')
students_df = pd.read_csv('data/students.txt', sep=',')

merged_df = pd.merge(grades_df, students_df, on='student_id')

# Calculating the average grade per student

avg_grade = merged_df[['student_id', 'grade']].groupby('student_id').mean()
print('Average grade per student is:', avg_grade)

# Finding the average grade per major

avg_major = merged_df[['major', 'grade']].groupby('major').mean()
print('Average grade per major is:', avg_major)

# Identifying students that has all grades above 85

merged_df['over 85'] = merged_df['grade'] > 85
over_85 = merged_df[['name', 'over 85']].groupby('name').all()

print('Students that have all grades above 85:', over_85)