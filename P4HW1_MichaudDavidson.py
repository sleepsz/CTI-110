# Davidson Michaud
# 11/5/2026
# P4HW1
# Use loops to collect and validate scores, then display results

'''
Ask user for number of scores
Loop to get each score
If score is invalid, loop until valid
Add score to list
Get lowest score and remove it
Get average of remaining scores
Determine letter grade
Display results
'''

# Get number of scores
num_scores = int(input("How many scores do you want to enter? "))
print()

scores_list = []

# Loop to collect each score
for num in range(1, num_scores + 1):
    score = float(input(f"Enter score #{num}: "))

    # Validate score between 0 and 100
    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{num} again: "))

    # Add score to list 
    scores_list += [score]

# Drop lowest score
lowest_score = min(scores_list)
scores_list.remove(lowest_score)

# Get the average
average = sum(scores_list) / len(scores_list)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print()
print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")
