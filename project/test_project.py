from project import get_calories, calculate_total_calories


def main():
    test_get_calories()
    test_calculate_total_calories()


def test_get_calories():
    # Test known foods
    assert get_calories("greek yoghurt") == 110
    assert get_calories("banana") == 105
    assert get_calories("salmon") == 356
    assert get_calories("kinder chocolate") == 118

    # Test unknown food
    assert get_calories("unknown food") == 0

    # Test case insensitivity
    assert get_calories("GREEK YOGHURT") == 110
    assert get_calories("BaNaNa") == 105
    assert get_calories("SaLmOn") == 356


def test_calculate_total_calories():
    # Test single food
    meal = {"greek yoghurt": 1}
    assert calculate_total_calories(meal) == 110

    # Test multiple food
    meal = {"greek yoghurt": 1, "banana": 2, "salmon": 1}
    assert calculate_total_calories(meal) == 110 + 2 * 105 + 356

    # Test unknown food
    meal = {"unknown food": 1}
    assert calculate_total_calories(meal) == 0

    # Test zero quantity
    meal = {"greek yoghurt": 0}
    assert calculate_total_calories(meal) == 0


if __name__ == "__main__":
    main()