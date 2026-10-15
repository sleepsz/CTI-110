'''
Davidson Michaud
10/06/26
P3LAB
Determine the most efficient coin combination
'''
# Get amount of money
money = float(input("Enter the amount of money: $"))

# Convert money into a integer
money_int = int(money * 100)

print("Amount as a whole number:", money_int)

# Determine how many dollars are needed
dollars = money_int // 100
remaining_money = money_int % 100
print("dollars:", dollars)

# Determine how many quarters are needed
quarters = remaining_money // 25
remaining_money = remaining_money % 25
print("Quarters:", quarters)

# Determine how many dimes are needed
dimes = remaining_money // 10
remaining_money = remaining_money % 10
print("Dimes:", dimes)

# Determine how many nickles are needed
nickles = remaining_money // 5
remaining_money = remaining_money % 5
print("Nickles:", nickles)

# Determine how many pennies are needed
pennies = remaining_money
print("Pennies:", pennies)

print()
print("--------------------------------------------------")
print()

def display_coins(coin, coin_name):
    if coin > 0:
        if coin == 1:
            print(f"1 {coin_name}")
        if coin > 1:
            print(f"{coin} {coin_name}s")
# Call the display_coin function for each coin
display_coins(dollars, "Dollar")
display_coins(quarters, "Quarter")
display_coins(dimes, "Dime")
display_coins(nickles, "Nickle")
display_coins(pennies, "Pennie")
