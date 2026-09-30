'''
Davidson Michaud
9/24/2026
P2HW1
Nicely format P1HW2
'''

# User enter their budget
print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()

# User enter their travel destination
Travel = str(input("Enter your travel destination: "))
print()
# User enter how much they will spend on gas
gasbudget = float(input("How much do you think you will spend on gas? "))
print()

## User enter how much they will spend on on accomodation
accomodation = float(input("How much do you think you will need for accomodation/hotel? "))
print()

# User enter food budget
food = float(input("Lastly, how much do you need for food? "))
print()

print("----- Travel Expenses ------")
#Display output with formatting widths
print(f"{'Location:':<20}{Travel}")
print(f"{'Initial budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gasbudget:.2f}")
print(f"{'Accomodation:':<20}${accomodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print()

# Calculate the cost of everything - the inital budget
prices = food + accomodation + gasbudget
final = budget - prices

print("----------------------")
print()
print(f"{'Remaining Balance:':<20}${final:.2f}")
