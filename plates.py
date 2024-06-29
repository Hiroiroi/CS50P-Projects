def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vanity plates contain max 6 characters and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Numbers can't be used in middle of a plate, must come at the end
    # First number used cannot be a '0'
    i = 0
    while i < len(s):
        if s[i].isalpha() == True:
            i += 1
        else:
            while i < len(s):
                if s[i].isalpha() == False:
                    i += 1
                else:
                    return False
                if s[i] == "0":
                    return False
                else:
                    break
            i += 1

    # No periods, spaces, or punctuation marks
    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

    # If all tests passed - return True
    return True

main()
