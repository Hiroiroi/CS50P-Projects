import inflect
p = inflect.engine()
# Create list to keep track of names
names = []
# Loop forever
while True:
    try:
        # Get user input
        user_input = input("Name: ")
        names.append(user_input)
    except EOFError:
        # Create new line and stop loop
        print()
        break
# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)
