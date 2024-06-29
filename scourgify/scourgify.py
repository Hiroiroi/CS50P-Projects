import sys
import csv

try:

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        beforeFile = sys.argv[1]
        afterFile = sys.argv[2]

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

originalFile = []

with open(beforeFile) as file:
    reader = csv.DictReader(file)
    for line in reader:
        lname, fname = line["name"].split(", ")
        house = line["house"]
        originalFile.append({"first": fname, "last": lname, "house": house})

print(originalFile)

# write to new file

with open(afterFile, "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in originalFile:
        writer.writerow(row)