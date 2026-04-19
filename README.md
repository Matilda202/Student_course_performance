# Student Course Performance

A pandas practice project that analyses student grades across multiple courses, using a merge to combine two related datasets.

## Files

| File | Description |
|---|---|
| `data/students.txt` | `student_id`, `name`, `major`, `year` |
| `data/grades.txt` | `student_id`, `course`, `grade` |
| `performance_analys.py` | Analysis script |

## Dataset overview

5 students. Majors: Computer Science, Mathematics, Physics. 8 grade rows across 5 courses (Programming I, Math I, Statistics, Physics I, Databases).

## Tasks completed

| # | Task | Pandas technique |
|---|---|---|
| 1 | Load both data files | `pd.read_csv()` |
| 2 | Combine student info with grades | `pd.merge(grades_df, students_df, on='student_id')` |
| 3 | Average grade per student | `groupby('student_id').mean()` |
| 4 | Average grade per major | `groupby('major').mean()` |
| 5 | Students with every grade above 85 | Boolean column + `groupby('name').all()` |

## Key code patterns

```python
# Merge two DataFrames on a shared key
merged = pd.merge(grades_df, students_df, on='student_id')

# Average per student
merged.groupby('student_id')['grade'].mean()

# Average per major
merged.groupby('major')['grade'].mean()

# Flag rows, then check that ALL rows in each group are True
merged['over_85'] = merged['grade'] > 85
merged.groupby('name')['over_85'].all()
```

## What to improve

- **Use `student_id` for grouping but display by `name`** — currently the average-grade summary uses `student_id` as the group key; merging back or using `name` directly makes the output easier to read.
- **Boolean column naming** — `'over 85'` (with a space) is awkward to access; rename to `'over_85'`.
- **Print descriptive labels** before each result so the console output is self-explanatory.
- **Filter the final result** — `groupby('name').all()` returns a row for every student (True or False). Add `.loc[lambda x: x]` or boolean indexing to print only the students who meet the threshold.
- **Script filename note** — the file is named `performance_analys.py` (shortened). Consider renaming to `performance_analysis.py` for clarity.

## How to run

```bash
pip install pandas
cd Student_course_performance
python performance_analys.py
```
