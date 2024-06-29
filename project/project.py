def get_calories(food):
    # Dictionary mapping food items to their respective calorie counts
    calorie_dict = {
        "greek yoghurt": 110,
        "banana": 105,
        "rock melon": 50,
        "mandarin": 40,
        "salmon": 356,
        "white rice": 206,
        "vogel's bread": 163,
        "cheese": 150,
        "egg": 78,
        "milk": 155,
        "avocado": 120,
        "kinder chocolate": 118
    }

    food_lower = food.lower()
    if food_lower in calorie_dict:
        return calorie_dict[food_lower]
    else:
        return 0  # Return 0 if the food item is not found in the dictionary


def calculate_total_calories(meal):
    total_calories = 0
    for food, quantity in meal.items():
        total_calories += get_calories(food) * quantity
    return total_calories


def get_user_input():
    meal = {}
    while True:
        food = input("Enter a food item eaten (or 'done' to finish): ").strip()
        if food.lower() == "done":
            break
        quantity = int(input("Enter servings of {} eaten: ".format(food)))
        meal[food] = quantity
    return meal


def main():
    print("Hello! What did you have to eat?")
    meal = get_user_input()
    total_calories = calculate_total_calories(meal)
    print("Total calories in the meal:", total_calories)


if __name__ == "__main__":
    main()
