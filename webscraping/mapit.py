# mapit,py - launches a map in a
# browser using an address from the command line

import webbrowser, sys
import pyperclip

prefix = "https://www.google.com/maps/place/"
# If there are arguements, use args as address
# If there are no arguments, grab from clipboard
if len(sys.argv) > 1:
    name = 1
    address = " ".join(sys.argv[1:])

else:
    address = pyperclip.paste()
    webbrowser.open(prefix + address)

webbrowser.open(prefix + address)
# TODO: Get the address from the cliboard.
