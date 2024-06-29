import requests
import sys
import json

try:
    # only accepts two arguments e.g., bitcoin.py 4
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        # convert to float
        sys.argv[1] = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

object = response.json()

rate = object["bpi"]["USD"]["rate_float"]

num = sys.argv[1]

amount = num * rate

print(f"${amount:,.4f}")

# import modules: requests, sys, json
# user input: how many bit coin
# error check:
# exit if user doesn't supply argument
# exit if not convertable to float
# exit if ValueError

# obtain raw bitcoin price
# save json response to variable
# access the dictionary and save to variable "rate"
# remove comma from conversion

# calculate rate and print to screen
