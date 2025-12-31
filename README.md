# Student Grades Analysis (Pandas Practice)

This mini project is a simple, real-world style exercise to practice working with **multiple CSV files** using **pandas**, including merging datasets and computing summary statistics.

## Files

- `students.csv`  
  Contains student information (id, name, major, year)

- `grades.csv`  
  Contains course grades for students (student_id, course, grade)

## Tasks

1. **Load both CSV files using pandas**
   - Read `students.csv` and `grades.csv` into DataFrames.

2. **Combine student info with grades**
   - Merge/join the two DataFrames using `student_id`.

3. **Calculate the average grade per student**
   - For each student, calculate their mean grade across all courses.

4. **Find the average grade per major**
   - For each major, calculate the average grade (based on all grades of students in that major).

5. **Identify students with all grades above 85**
   - Find students whose **every** grade is **strictly greater than 85**.
   - (Tip: This is a group-level condition, not row-level.)

## Expected Skills Practiced

- `pd.read_csv()`
- `merge()` / joins
- `groupby()` + aggregations (`mean`, `all`, etc.)
- boolean filtering
- basic DataFrame inspection and printing

## How to Run

1. Install dependencies:
   pip install pandas

2. Run your script:
   python performance_analysis.py
