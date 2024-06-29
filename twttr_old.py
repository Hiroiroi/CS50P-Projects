# Request user for input
user_input = input("Input: ")

# Print "Output: "
print("Output: ", end="")

# Iterate through each letter of input
for letter in user_input:

    # Check 'if not' vowels contained in input
    if not letter.lower() in ["a", "e", "i", "o", "u"]:

        # Print letter
        print(letter, end="")

# Print new line
print()


