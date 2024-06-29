from tabulate import tabulate
import sys
import csv

table = []

if len(sys.argv) < 2: # python pizza.py sicilian.csv
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    csvFile = sys.argv[1]
    try:
        if csvFile.endswith("csv"):
            with open(csvFile) as file:
                reader = csv.reader(file)
                for row in reader:
                    table.append(row)
                print(tabulate(table, tablefmt="grid", headers="firstrow"))

        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

