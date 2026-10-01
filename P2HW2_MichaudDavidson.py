'''
Davidson Michaud
9/24/2026
P2HW2 
Use a dictionary to determine car mpg
'''
# Get 6 scores from user
grade1 = float(input("Enter score 1: "))
grade2 = float(input("Enter score 2: "))
grade3 = float(input("Enter score 3: "))
grade4 = float(input("Enter score 4: "))
grade5 = float(input("Enter score 5: "))
grade6 = float(input("Enter score 6: "))

# Put grades into a list
grades_list = [grade1, grade2, grade3, grade4, grade5, grade6]

print("-------Results----------")
print()

# Get the lowest grade
print(f"Lowest grade: {min(grades_list)}")

# Get highest grade
print(f"Highest grade: {max(grades_list)}")

# Get the sum of the grades
print(f"Sum of grade: {sum(grades_list)}")

# Get the average
average =sum(grades_list) / len(grades_list)
print(f"Average: {average:.1f}")


print("---------------------------------")