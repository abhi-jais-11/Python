# Define the height of the pattern
height = 7

# T pattern
for i in range(height):
    if i == 0:
        print("*" * height)  # Top horizontal line
    else:
        print(" " * (height // 2) + "*")  # Vertical line in the center

# Blank line to separate


# U pattern
for i in range(height):
    if i == height - 1:
        print("*" * height)  # Bottom horizontal line
    else:
        print("*" + " " * (height - 2) + "*")  # Vertical lines at both ends

# Blank line to separate



# L pattern
for i in range(height):
    if i == height - 1:
        print("*" * height)  # Bottom horizontal line
    else:
        print("*")  # Vertical line

# Blank line to separate



# S pattern
for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * height)  # Top and bottom horizontal lines
    elif i == height // 2:
        print("*" * (height//2+4))  # Middle horizontal line (shorter)
    elif i<height//2:
        print("*")  # Vertical lines
    else:
         print(" "*6 +"*")

# Blank line to separate



# I pattern
for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * height)  # Top and bottom horizontal lines
    else:
        print(" " * (height // 2) + "*")  # Vertical line in the center
