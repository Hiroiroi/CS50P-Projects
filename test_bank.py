from bank import value


def main():
    test_value1()
    test_value2()
    test_value3()


def test_value1(): # $0
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("    hello   ") == 0


def test_value2(): # $20
    assert value("hi") == 20
    assert value("heavy") == 20
    assert value("   Helo   ") == 20


def test_value3(): # $100
    assert value("goodday") == 100
    assert value("CS50") == 100
    assert value("    Chur   ") == 100


if __name__ == "__main__":
    main()