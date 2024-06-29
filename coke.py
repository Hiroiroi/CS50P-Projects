# Variable to keep track of amount owed
amount_owed = 50

# Loop until amount_due is > 0
while amount_owed > 0:

    # Print amount due
    print("Amount Due: ", amount_owed)
    # Ask user to insert coin(s)
    coin = int(input("Insert Coin: "))
    # Check if coin is 25, 10, or 5 cents
    if coin in [25, 10, 5]:
        # Subtract value from amount_due
        amount_owed -= coin

# Calculate change_owed
change_owed = abs(amount_owed)

# Print result
print("Change Owed: ", change_owed)
