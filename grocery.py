# Create empty dict
shopping_list = {}
# Loop forever
while True:
    try:
        # Get user input
        item = input().lower()
        # Check if item already in dict
        if item in shopping_list:
            # If it is, add 1 in the count
            shopping_list[item] += 1
        # Otherwise, add item for the first time
        else:
            shopping_list[item] = 1
    # can detect when user has inputted control-d by catching EOFError
    except EOFError:
        # Print all items in alphabetical order
        for key in sorted(shopping_list.keys()):
            print(shopping_list[key], key)
        # Stop the while loop
        break