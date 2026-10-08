# Davidson Michaud
# 10/6/26
# Use if/else statements to determine overtime pay
#P3HW2

# python -m streamlit run P3HW2_MichaudDavidson.py

import streamlit as st

st.title("PayCheck Calculator")

# Get name
name = st.text_input("Enter employee name: ")

# Get hour worked
hours_worked = st.number_input("Enter hours worked: ")

# Get pay rate
pay_rate = st.number_input("Enter your pay rate: $")

if hours_worked > 40:
    print("You had some overtime")
    OT_hours = hours_worked - 40
    reg_hours = 40
    OT_pay = (pay_rate * 1.5) * OT_hours
    reg_pay = reg_hours * pay_rate
    pay_day = reg_pay + OT_pay

else: # If they worked 40 hours or less
    print("You did not have any overtime")
    OT_hours = 0
    reg_hours = hours_worked
    OT_pay = 0
    reg_pay = reg_hours * pay_rate
    pay_day = reg_pay
    
# Display results / (st.write is basically print)
st.write(f"Hours worked: {hours_worked:.1f}")
st.write(f"Pay rate: ${pay_rate:.2f}")
st.write(f"Overtime Hours: {OT_hours:.1f}")
st.write(f"Overtime Pay: ${OT_pay:.2f}")
st.write(f"Normal pay: ${reg_pay:.2f}")
st.write(f"-----------")
st.write(f"Gross pay (Pay Day!): ${pay_day:.2f}")


    