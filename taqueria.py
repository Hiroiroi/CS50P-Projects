food_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        item = input("Item: ").title()
        if item in food_menu:
            total += food_menu[item]
            print("Total: $", end="")
            print("{:.2f}".format(total))
    except EOFError:
        print()
        break

