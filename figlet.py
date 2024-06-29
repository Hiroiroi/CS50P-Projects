import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    # exit(1) means there was some issue / error / problem and that is why the program is exiting.
    print("Invalid usage")
    sys.exit(1)

# retrieve list of available fonts
figlet.getFonts()

if not isRandomFont:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

user_input = input("Input: ")

print("Output:")
print(figlet.renderText(user_input))

