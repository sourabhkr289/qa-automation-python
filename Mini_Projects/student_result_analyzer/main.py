import config

# Input marks
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

# Total calculation
total = m1 + m2 + m3

# Average
average = total / config.TOTAL_SUBJECTS

# Percentage
percentage = (total / (config.TOTAL_SUBJECTS * config.MAX_MARKS_PER_SUBJECT)) * 100

# Pass/Fail check (logical + comparison)
if m1 >= config.PASS_MARK and m2 >= config.PASS_MARK and m3 >= config.PASS_MARK:
    result = "Pass"
else:
    result = "Fail"

# Grade calculation
if percentage >= config.GRADE_A:
    grade = "A"
elif percentage >= config.GRADE_B:
    grade = "B"
elif percentage >= config.GRADE_C:
    grade = "C"
else:
    grade = "Fail"

# Highest & Lowest marks
highest = max(m1, m2, m3)
lowest = min(m1, m2, m3)

# Output
print("\n----- Result -----")
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Result:", result)
print("Grade:", grade)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)