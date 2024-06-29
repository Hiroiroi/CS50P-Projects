import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M)"
    if times := re.search(r"^" + regex + " to " + regex + "$", s):
        t = times.groups()
        return f"{convert_time(t[:3])} to {convert_time(t[3:])}"
    raise ValueError


def convert_time(time):
    # time is a list where the index [0] is for hours, [1] for minutes (or None), [2] for AM or PM
    if time[0] == "12":
        hours = "00" if time[2] == "AM" else "12"
    else:
        hours = f"{int(time[0]):02}" if time[2] == "AM" else f"{int(time[0]) + 12}"
    minutes = "00" if time[1] == None else f"{int(time[1]):02}"
    return hours + ":" + minutes


if __name__ == "__main__":
    main()
