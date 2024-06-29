from seasons import check_birthday


def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday('1994-07-07') == ("1994", "07", "07")
    assert check_birthday('1994-7-7') is None
    assert check_birthday("July 7, 1994") is None

    if __name__ == "__main__":
        main()
