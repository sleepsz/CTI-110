# Davidson Michaud
# 11/5
# P4LAB2 
# Loops that display multiplication
'''
Get integer from user
Determine if integer is positive or negative
if number is postive, display multiplacation table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program
If no, end program
'''

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >=0:
        #Display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print (f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative number")
        
    run_again = input("Would you like to run this program again? ")
    
# Loop has broken (user enter no)
print("Program is ending")