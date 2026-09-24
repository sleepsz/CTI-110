'''
Davidson Michaud
9/24/2026
P1HW2
create a program that does some basic math on numbers that are entered.
'''
# User enter their budget
print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
# User enter their travel destination
Travel = str(input("Enter your travel destination: "))
print()
# User enter how much they will spend on gas
gasbudget = int(input("How much do you think you will spend on gas? "))
print()
## User enter how much they will spend on on accomodation
accomodation = int(input("How much do you think you will need for accomodation/hotel? "))
print()
# User enter food budget
food = int(input("Lastly, how much do you need for food? "))
print()
print("----- Travel Expenses ------")

#Display output
print(f"Location: {Travel}")
print(f"Initial budget: {budget}")
print()
print(f"Fuel: {gasbudget}")
print(f"Accomodation: {accomodation}")
print(f"Food: {food}")
print()
# Calculate the cost of everything - the inital budget
prices = food + accomodation + gasbudget
final = budget - prices

print(f"Remaining Balance: {final}")
