# Davidson Michaud
# 9/15/2026
# P1HW1
# Performing math calculation

print("-----Calculating Exponents-----")
print()
print()

# Get integer values from user
base_value = int(input("Enter the base value: "))
exponent = int(input("Enter the exponent value: "))
# Calculate the answer
answer = base_value ** exponent

# Show datatype of a specific variable  
#print(type(answer))

# Display the actual answer to the user
print(base_value, "raised to the power of", exponent, "is", answer, "!!")

# Addition and Subtraction Part 
print() 
print() 
print("-----Addition and Subtraction-----") 
print() 
print() 

# Values
starting_value = int(input("Enter the starting value: "))
adding_value = int(input("Enter an integer to add: "))
subtracting_value = int(input("Enter an integer to subtract: "))

# Calculate 
finish = starting_value + adding_value - subtracting_value

# Output Result
print(starting_value, "+", adding_value, "-", subtracting_value, "is equal to", finish)
