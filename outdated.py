months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop forever
while True:

    # Get user input
    date = input("Date: ").strip()
    try:
        # Split the date by /
        month, day, year = date.split("/")
        # Check if month is in between 1 and 12, day is between 1 and 31
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        try:
            if "," not in date:
                raise SyntaxError
            # Split the date by space
            old_month, old_day, year = date.split(" ")
            # Find number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
            # Remove comma from day variable
            day = old_day.replace(",", "")
            # Check if month between 1-12 and day between 1-31
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
