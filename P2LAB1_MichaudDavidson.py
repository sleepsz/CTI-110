import math
'''
Davidson Michaud
9/24/2026
Using math library to calculate circle features
'''

# Get radius from user as float
radius = float(input("Enter the radius as a float: "))
print()

# Calculate the diameter
diameter = 2 * radius

#Display diameter using the f-string (formatting) (.1f shows how many places after decimal point (.1f=1 decimal))
print(f"The diameter of the circle is {diameter:.1f}")
print()

# Calculate the circumference
circumference = 2 * math.pi * radius
# Display circumference
print(f"The circumference of the circle is {circumference:.2f}")

print()

#Calculate the area (math.pow(x.y))
area = math.pi * radius ** 2
# Display the area
print(f"The area of the circle is {area:.3f}")