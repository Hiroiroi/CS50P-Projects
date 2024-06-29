def main(): # engine
    loop = True
    while loop:
        try:

            fraction = input("Fraction: ")
            percentage = convert(fraction)
            result = gauge(percentage)
            loop = False
            print(result)

        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction): # convert fraction to percentage
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    percent = x/y

    if percent > 1: # re-prompts if > 1
        main()

    else: # convert function
        percent = percent * 100
        percent = round(percent)
        return percent


def gauge(percentage): # do the calculations
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()